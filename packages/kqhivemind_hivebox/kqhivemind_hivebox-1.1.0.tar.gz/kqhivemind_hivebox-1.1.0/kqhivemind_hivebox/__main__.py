import collections
import json
import logging
import math
import signal
import string
import subprocess
import sys
import threading
import time
from datetime import datetime, timedelta

import gpiod
import nfc
import requests
import websocket
from nfc.clf import ContactlessFrontend, transport
from nfc.clf.acr122 import Chipset, Device
from py532lib.mifare import MIFARE_SAFE_RETRIES, Mifare

from .__version__ import __version__
from .constants import HOLD_TIME, PIN_ORDER, POSITION_NAME
from .gpio import GPIO
from .lcddriver import LCD
from .util import get_position_id
from .gamestate import GameState


def format_time(seconds):
    return "{}:{:02d}".format(int(seconds/60), int(seconds%60))

def main():
    state = {
        "card": None,
        "time": None,
        "last_card": None,
        "last_card_time": None,
        "register_data": None,
        "register_time": None,
        "register_complete_time": None,
        "startup_time": None,
        "cabinet_id": None,
        "lights_on": {},
        "initialized": set(),
        "initialized_time": None,
        "buttons": {},
        "lights": {},
        "button_held": {},
        "clip_requested_time": None,
        "api_requests": collections.deque(),
        "players_with_pending_requests": {},
        "wifi_name": None,
        "no_wifi": False,
        "cabinet_name": None,
        "sign_in_name": {},
        "sign_in_time": {},
        "wifi_added_name": None,
        "wifi_added_time": None,
        "ws_close_time": None,
    }

    with open(sys.argv[1]) as in_file:
        settings = json.load(in_file)

    DOMAIN = settings.get("domain", "kqhivemind.com")
    IS_SECURE = settings.get("secure", True)
    PORT = settings.get("port", 443 if IS_SECURE else 80)
    API_PROTOCOL = "https" if IS_SECURE else "http"
    API_BASE_URL = f"{API_PROTOCOL}://{DOMAIN}:{PORT}/api"
    API_URL = f"{API_BASE_URL}/stats/signin/nfc/"
    WS_PROTOCOL = "wss" if IS_SECURE else "ws"
    WS_URL = f"{WS_PROTOCOL}://{DOMAIN}:{PORT}/ws/signin"
    USE_GPIO = "pin_config" in settings
    DRIVER = settings.get("driver", "acr1252u")

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("[%(asctime)s]  %(message)s")

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if settings.get("log_file"):
        file_handler = logging.FileHandler(settings.get("log_file"))
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


    if USE_GPIO:
        gpio = GPIO(settings)

    def register_card(card_id, register_data):
        data = {
            "action": "nfc_register_tapped",
            "card": card_id,
            **register_data,
        }

        state["api_requests"].append(data)

    def sign_in(card_id, player_id):
        if settings.get("test_mode"):
            light_pins = { i["player_id"]: i["light"] for i in settings["pin_config"] }
            pin = light_pins.get(int(player_id))
            if pin:
                state["lights_on"][pin] = True

            return

        data = {
            "action": "sign_in",
            "card": card_id,
            "player": player_id,
        }

        state["api_requests"].append(data)
        state["players_with_pending_requests"][player_id] = datetime.now()

    def sign_out(player_id):
        if settings.get("test_mode"):
            light_pins = { i["player_id"]: i["light"] for i in settings["pin_config"] }
            pin = light_pins.get(int(player_id))
            if pin:
                state["lights_on"][pin] = False

            return

        data = {
            "action": "sign_out",
            "player": player_id,
        }

        state["api_requests"].append(data)
        state["players_with_pending_requests"][player_id] = datetime.now()

    def create_clip(player_id):
        logger.info("Creating Twitch clip from player {}".format(player_id))
        state["clip_requested_time"] = datetime.now()

        user_id = None
        cabinet_id = get_cabinet_id()

        url = f"{API_BASE_URL}/game/cabinet/{cabinet_id}/signin/"
        req = requests.get(f"{API_BASE_URL}/game/cabinet/{cabinet_id}/signin/")
        for user in req.json()["signed_in"]:
            if user["player_id"] == player_id:
                user_id = user["user_id"]

        postdata = {
            "cabinet": cabinet_id,
            "token": settings["token"],
            "created_by": user_id,
        }

        req = requests.post(f"{API_BASE_URL}/video/video-clip/", data=postdata)

    def card_read(uid):
        if state["last_card"] == uid and state["last_time"] and \
           state["last_time"] > datetime.now() - timedelta(seconds=10):
            return

        logger.info("Card read: UID {}".format(uid))

        if state["register_data"] and state["register_time"] and \
           state["register_time"] > datetime.now() - timedelta(minutes=1):

            register_card(uid, state["register_data"])
            state["register_data"] = None
            state["register_complete_time"] = datetime.now()
            state["last_card"] = uid
            state["last_time"] = datetime.now()
            return

        state["last_card"] = state["card"] = uid
        state["last_time"] = state["time"] = datetime.now()

    def listen_card():
        if DRIVER == "acr1252u":
            return listen_card_acr1252u()
        if DRIVER == "pn532_i2c":
            return listen_card_pn532_i2c()

    def listen_card_acr1252u():
        chipset = Chipset.__new__(Chipset)
        found = transport.USB.find(settings["usb_device"])
        vid, pid, bus, dev = found[0]
        logger.warning("device {}: vid {}, pid {}, bus {}, dev {}".format(settings["usb_device"], *found[0]))
        chipset.transport = transport.USB(bus, dev)

        frame = bytearray.fromhex("62000000000000000000")
        chipset.transport.write(frame)
        chipset.transport.read(100)

        chipset.ccid_xfr_block(bytearray.fromhex("FF00517F00"))
        chipset.set_buzzer_and_led_to_default()

        device = Device.__new__(Device)
        device.chipset = chipset
        device.log = logger

        def connected(llc):
            card_read(llc.identifier.hex())

            chipset.ccid_xfr_block(bytearray.fromhex("FF00400D0403000101"), timeout=1)
            chipset.ccid_xfr_block(bytearray.fromhex("FF00400E0400000000"), timeout=1)

            while llc.is_present:
                time.sleep(0.1)

            return False

        while True:
            clf = ContactlessFrontend.__new__(ContactlessFrontend)
            clf.device = device
            clf.lock = threading.Lock()

            state["initialized"].add("card")

            try:
                clf.connect(rdwr={"on-connect": connected})
            except KeyboardInterrupt:
                clf.close()
            except Exception as err:
                logger.exception("Unhandled exception in on-connect: {}".format(err))
                time.sleep(1)

    def listen_card_pn532_i2c():
        mifare = Mifare()
        if "i2c_channel" in settings:
            mifare.i2c_channel = settings.get("i2c_channel")

        mifare.SAMconfigure()
        mifare.set_max_retries(MIFARE_SAFE_RETRIES)
        state["initialized"].add("card")

        while True:
            try:
                if state["card"] and state["time"] > datetime.now() - timedelta(seconds=15):
                    time.sleep(1)
                    continue

                uid = mifare.scan_field()
                if uid:
                    uid_hex = "".join('{:02x}'.format(i) for i in uid)
                    card_read(uid_hex)

            except KeyboardInterrupt:
                logger.warning("Keyboard interrupt")
                return
            except Exception as err:
                logger.exception("Unhandled exception in listen_card: {}".format(err))

            time.sleep(0.25)

    def player_id_by_button(button):
        if "player_ids_by_button" not in state:
            state["player_ids_by_button"] = {
                i["button"]: get_position_id(i, settings["reader"])
                for i in settings["pin_config"]
            }

        return state["player_ids_by_button"].get(button)

    def button_pressed(button):
        player_id = player_id_by_button(button)
        state["button_held"][player_id] = False
        logger.info("Button pressed on player {} ({})".format(player_id, button))

    def button_held(button):
        player_id = player_id_by_button(button)
        state["button_held"][player_id] = True
        logger.info("Button held on player {} ({})".format(player_id, button))
        if settings.get("enable_clipping"):
            create_clip(player_id)

    def button_released(button):
        player_id = player_id_by_button(button)
        logger.info("Button released on player {} ({})".format(player_id, button))
        if state["button_held"].get(player_id):
            return

        if state["card"] and state["time"] > datetime.now() - timedelta(seconds=15):
            sign_in(state["card"], player_id)
            state["card"] = None
            state["time"] = None
            state["register_data"] = None
            state["register_time"] = None
        else:
            sign_out(player_id)

    gpio.on_button_press(button_pressed)
    gpio.on_button_release(button_released)
    gpio.on_button_hold(button_held)

    def on_message(ws, message_text):
        try:
            logger.debug(message_text)
            message = json.loads(message_text)

            if settings.get("scene") and settings.get("cabinet"):
                if message.get("scene_name") != settings.get("scene") or \
                   message.get("cabinet_name") != settings.get("cabinet"):
                    return

            if settings.get("device"):
                if settings["device"] not in message.get("device_ids", {}) and \
                   settings["device"] != message.get("reader_id"):
                    return

            if message.get("type") == "nfc_register":
                state["register_data"] = {k: v for k, v in message.items()
                                          if k not in ["type", "scene_name", "cabinet_name", "reader_id"]}
                state["register_time"] = datetime.now()

                logger.info("Got register request: {}".format(
                    ", ".join([f"{k}={v}" for k, v in state["register_data"].items()]),
                ))

            else:
                player_id = int(message["player_id"])
                light_pins = { get_position_id(i, settings["reader"]): i["light"] for i in settings["pin_config"] }
                pin = light_pins.get(player_id)
                if pin:
                    value = message["action"] == "sign_in"
                    logger.info("Setting {} to {} (player {})".format(pin, value, player_id))
                    state["lights_on"][pin] = value

                    state["sign_in_time"][player_id] = datetime.now() if value else None
                    state["sign_in_name"][player_id] = message.get("user_name") if value else None

        except Exception as e:
            logger.exception("Exception in on_message")

    def send_api_requests():
        if len(state["api_requests"]) > 0:
            data = state["api_requests"].popleft()
            data["scene_name"] = settings.get("scene")
            data["cabinet_name"] = settings.get("cabinet")
            data["device_id"] = settings.get("device")
            data["token"] = settings["token"]

            try:
                req = requests.post(API_URL, json=data, timeout=10)
                req.raise_for_status()
            except:
                state["api_requests"].insert(0, data)

            if "player" in data and data["player"] in state["players_with_pending_requests"]:
                del state["players_with_pending_requests"][data["player"]]

        if state["register_data"] and state["register_data"].get("user") and "user_name" not in state["register_data"]:
            req = requests.get(f"{API_BASE_URL}/user/user/{state['register_data']['user']}/public-data/")
            state["register_data"]["user_name"] = req.json()["name"]


    def send_api_requests_thread():
        while True:
            try:
                send_api_requests()
            except Exception as e:
                logger.exception(e)

            time.sleep(0.1)

    def on_ws_error(ws, error):
        logger.error("Error in websocket connection: {}".format(error))
        ws.close()

    def on_ws_close(ws, close_status_code, close_msg):
        state["ws_close_time"] = datetime.now()
        logger.error("Websocket closed ({})".format(close_msg))

    def get_cabinet_id():
        if state.get("cabinet_id"):
            return state["cabinet_id"]

        if settings.get("scene") and settings.get("cabinet"):
            req = requests.get(f"{API_BASE_URL}/game/scene/", params={"name": settings["scene"]})
            scene_id = req.json()["results"][0]["id"]

            req = requests.get(f"{API_BASE_URL}/game/cabinet/",
                               params={"scene": scene_id, "name": settings["cabinet"]})
            cabinet_id = req.json()["results"][0]["id"]
            state["cabinet_id"] = cabinet_id
            state["cabinet_name"] = req.json()["results"][0]["display_name"]

            return cabinet_id

    def set_lights_from_api():
        if settings.get("test_mode"):
            return

        cabinet_id = get_cabinet_id()

        if cabinet_id:
            req = requests.get(f"{API_BASE_URL}/game/cabinet/{cabinet_id}/signin/")
            signed_in = {get_position_id(i, settings["reader"]) for i in req.json()["signed_in"]}

        elif settings.get("device"):
            device_id = settings["device"]
            req = requests.get(f"{API_BASE_URL}/game/client-device/{device_id}/signin/")

        if req:
            signed_in = {get_position_id(i, settings["reader"]) for i in req.json()["signed_in"]}

            for row in settings["pin_config"]:
                if get_position_id(row, settings["reader"]) and row.get("light"):
                    value = get_position_id(row, settings["reader"]) in signed_in
                    state["lights_on"][row["light"]] = value

    def set_lights():
        logger.info("Starting lights thread.")

        while True:
            mode = None
            blink_rate = 1
            animation_time = None

            if "card" in state["initialized"] and "websocket" in state["initialized"]:
                if state["initialized_time"] is None:
                    state["initialized_time"] = time.monotonic()

                if state["initialized_time"] > time.monotonic() - 3.0:
                    mode = "sweep"
                    animation_time = state["initialized_time"]

            if state["card"] and state["time"] > datetime.now() - timedelta(seconds=15):
                mode = "blink"
                blink_rate = 6

            if state["register_data"] and state["register_time"] and \
               state["register_time"] > datetime.now() - timedelta(minutes=1):
                mode = "blink"
                blink_rate = 2

            if state["register_complete_time"] and \
               state["register_complete_time"] > datetime.now() - timedelta(seconds=0.75):
                mode = "happy"
                animation_time = state["register_complete_time"]

            if state["clip_requested_time"] and \
               state["clip_requested_time"] > datetime.now() - timedelta(seconds=0.75):
                mode = "happy"
                animation_time = state["clip_requested_time"]

            for pin in filter(lambda i: i.get("light"), settings["pin_config"]):
                if mode == "blink":
                    if(state["lights_on"].get(pin["light"])):
                        value = 1.0
                    else:
                        value = (math.sin(time.monotonic() * blink_rate) + 1) * .5

                elif mode == "sweep":
                    t = time.monotonic()
                    idx = PIN_ORDER.get(get_position_id(pin, settings["reader"]), 0)
                    on_time = animation_time + (idx * 0.1)
                    fade_time = on_time + 0.2
                    off_time = on_time + 0.6
                    if t > on_time and t < fade_time:
                        value = 1.0
                    elif t > fade_time and t < off_time:
                        value = ((1 - (t - fade_time)) / (off_time - fade_time))
                    else:
                        value = 0

                elif mode == "happy":
                    frame = math.floor((datetime.now() - animation_time) / timedelta(seconds=0.15))
                    frames_on_by_idx = {
                        1: {2},
                        2: {1, 3},
                        3: {0, 4},
                        4: {1, 3},
                        5: {2},
                    }

                    idx = PIN_ORDER.get(get_position_id(pin, settings["reader"]), 0)
                    value = 1.0 if frame in frames_on_by_idx.get(idx, {}) else 0

                elif mode == "bounce":
                    frame = math.floor((datetime.now() - animation_time) / timedelta(seconds=0.15)) % 16
                    frames_on_by_idx = {
                        1: {0, 1, 15},
                        2: {1, 2, 3, 13, 14, 15},
                        3: {3, 4, 5, 11, 12, 13},
                        4: {5, 6, 7, 9, 10, 11},
                        5: {7, 8, 9}
                    }

                    idx = PIN_ORDER.get(get_position_id(pin, settings["reader"]), 0)
                    value = 1.0 if frame in frames_on_by_idx.get(idx, {}) else 0

                elif state["players_with_pending_requests"].get(get_position_id(pin, settings["reader"]), datetime.min) > datetime.now() - timedelta(seconds=10):
                    value = 1.0 if time.monotonic() % 0.5 < 0.25 else 0.0

                else:
                    value = 1.0 if state["lights_on"].get(pin["light"], False) else 0

                value = float(min(max(value, 0.0), 1.0))
                gpio.brightness[pin["light"]] = value

            time.sleep(0.01)

    def listen_ws():
        if settings.get("test_mode"):
            state["initialized"].add("websocket")
            return

        logger.info("Starting websocket thread.")

        while True:
            try:
                if USE_GPIO:
                    set_lights_from_api()

                wsapp = websocket.WebSocketApp(
                    WS_URL,
                    on_message=on_message,
                    on_error=on_ws_error,
                    on_close=on_ws_close,
                )

                logger.info("Websocket connection online.")
                state["ws_close_time"] = None
                state["initialized"].add("websocket")
                wsapp.run_forever(
                    ping_interval=15,
                    ping_timeout=5,
                )

            except Exception as e:
                logger.exception("Exception in wsapp.run_forever")

            time.sleep(1)

    def listen_gamestate():
        gamestate = GameState(state, settings)
        gamestate.listen()

    def spinner():
        chars = [chr(i) for i in [161, 165, 223, 32]]
        idx = int((3 * time.monotonic()) % len(chars))
        return chars[idx]

    def printable(text):
        return "".join([i for i in text if i in set(string.printable)])

    def get_scrolling_text_part(text, max_chars):
        if len(text) <= max_chars:
            return text

        num_frames = 14 + len(text)
        idx = max(0, int((4 * time.monotonic()) % num_frames) - 10)

        return "{}    {}".format(text, text)[idx:idx+max_chars]

    def get_screen_text_from_state():
        if "websocket" not in state["initialized"]:
            return [
                "HiveBox {}".format(__version__),
                "Connecting... {}".format(spinner()),
            ]

        if "card" not in state["initialized"]:
            return [
                "HiveBox {}".format(__version__),
                "Start NFC... {}".format(spinner()),
            ]

        if state["card"] and state["time"] > datetime.now() - timedelta(seconds=15):
            return [
                "Card {}".format(state["card"]),
                "Press button",
            ]

        if state["wifi_added_name"] and state["wifi_added_time"] > datetime.now() - timedelta(seconds=10):
            return [
                "Added WiFi Net",
                get_scrolling_text_part(state["wifi_added_name"], 16),
            ]

        if state["register_data"] and state["register_time"] and \
           state["register_time"] > datetime.now() - timedelta(minutes=1):
            if state["register_data"].get("user_name"):
                return [
                    "Tap to register:",
                    get_scrolling_text_part(printable(state["register_data"]["user_name"]), 16),
                ]

            return [
                "Tap to register:",
                "User ID {}".format(state["register_data"].get("user")),
            ]

        sign_in_values = {
            k: v for k, v in state["sign_in_time"].items()
            if v and v > datetime.now() - timedelta(seconds=5)
        }

        if any(sign_in_values):
            position_id = sorted(sign_in_values.keys(), key=lambda i: sign_in_values[i], reverse=True)[0]
            name = state["sign_in_name"][position_id]

            if name:
                return [
                    "  On {}:".format(POSITION_NAME.get(position_id, position_id)),
                    printable(name),
                ]

        if state.get("team_name") and state.get("team_name_set", 0) > time.monotonic() - 300:
            if state.get("is_warmup") and state.get("game_running"):
                return [
                    get_scrolling_text_part(printable(state["team_name"]), 16),
                    "WARM-UP  {}".format(format_time(time.monotonic() - state["gamestart"])),
                ]

            if not state.get("game_running"):
                return [
                    get_scrolling_text_part(printable(state["team_name"]), 16),
                    "      " + state.get("match_score", ""),
                ]

        if len(state["sign_in_time"]) == 0 and state["startup_time"] > datetime.now() - timedelta(seconds=60):
            wifi_name_part = "No WiFi Found" if state["no_wifi"] else \
                "WiFi: {}".format(get_scrolling_text_part(state["wifi_name"], 10))

            if state["cabinet_name"]:
                return [
                    "HiveBox {}".format(__version__) if (time.monotonic() % 15) < 5 else wifi_name_part,
                    "Cab:  {}".format(get_scrolling_text_part(state["cabinet_name"], 10)),
                ]

            if settings.get("device"):
                return [
                    "HiveBox {}".format(__version__) if (time.monotonic() % 15) < 5 else wifi_name_part,
                    "ID:   {}".format(get_scrolling_text_part(settings.get("device", "???"), 10)),
                ]

            return [
                "Config Error",
                "No device or cab name",
            ]

        return [
            "",
            "",
        ]

    def set_screen():
        logger.info("Starting screen thread.")

        lcd = LCD(port=settings.get("i2c_channel"))
        lcd.set_backlight(True)
        lcd.display_string("Starting up...", 1)

        try:
            state["wifi_name"] = subprocess.check_output(["/usr/sbin/iwgetid", "-r"]).decode("utf-8").strip()
        except subprocess.CalledProcessError:
            state["no_wifi"] = True

        state["screen"] = get_screen_text_from_state()
        state["last_screen_change"] = time.monotonic()
        state["initialized"].add("screen")

        while True:
            new_text = get_screen_text_from_state()
            if new_text != state["screen"]:
                state["screen"] = new_text
                state["last_screen_change"] = time.monotonic()

                for idx, line in enumerate(new_text):
                    lcd.display_string("{: <16}".format(line), idx+1)

                if not any([i != "" for i in new_text]):
                    lcd.set_backlight(False)

            time.sleep(0.1)

    # Startup
    state["startup_time"] = datetime.now()

    card_thread = threading.Thread(target=listen_card, name="card", daemon=True)
    card_thread.start()

    ws_thread = threading.Thread(target=listen_ws, name="websocket", daemon=True)
    ws_thread.start()

    gamestate_thread = threading.Thread(target=listen_gamestate, name="gamestate", daemon=True)
    gamestate_thread.start()

    api_thread = threading.Thread(target=send_api_requests_thread, name="api", daemon=True)
    api_thread.start()

    screen_thread = threading.Thread(target=set_screen, name="screen", daemon=True)
    screen_thread.start()

    if USE_GPIO:
        lights_thread = threading.Thread(target=set_lights, name="lights", daemon=True)
        lights_thread.start()

    while True:
        time.sleep(1)

    logger.info("Exiting.")


if __name__ == "__main__":
    main()
