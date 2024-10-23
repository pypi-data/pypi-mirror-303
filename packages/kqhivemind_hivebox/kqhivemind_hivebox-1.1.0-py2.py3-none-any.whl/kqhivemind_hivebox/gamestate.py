import time
import logging
import websocket
import requests
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class GameState:
    def __init__(self, state, settings):
        super().__init__()
        self.state = state
        self.settings = settings
        self.cabinet_id = None
        self.cabinet_id_checked = None

        is_secure = settings.get("secure", True)
        domain = settings.get("domain", "kqhivemind.com")
        port = settings.get("port", 443 if is_secure else 80)
        api_protocol = "https" if is_secure else "http"
        ws_protocol = "wss" if is_secure else "ws"

        self.gamestate_url = f"{ws_protocol}://{domain}:{port}/ws/gamestate"
        self.api_base_url = f"{api_protocol}://{domain}:{port}/api"

    def on_message(self, ws, message_text):
        if self.cabinet_id_checked is None or self.cabinet_id_checked < time.monotonic() - 300:
            if self.settings.get("device"):
                device_id = self.settings.get("device")
                url = f"{self.api_base_url}/game/client-device/{device_id}/"
                response = requests.get(url)
                response.raise_for_status()

                data = response.json()
                self.cabinet_id = data.get("cabinet")
                self.cabinet_id_checked = time.monotonic()

            if self.settings.get("scene") and self.settings.get("cabinet"):
                scene = self.settings.get("scene")
                cabinet = self.settings.get("cabinet")

                url = f"{self.api_base_url}/api/game/cabinet/"
                response = requests.get(url, params={
                    "scene": self.settings["scene"],
                    "cabinet": self.settings["cabinet"],
                })
                response.raise_for_status()

                data = response.json()
                if data and len(data) > 0:
                    self.cabinet_id = data[0].get("id")

                self.cabinet_id_checked = time.monotonic()

        message = json.loads(message_text)
        if message.get("type") == "match" and message.get("cabinet_id") == self.cabinet_id:
            if message.get("current_match"):
                match = message["current_match"]

                self.state["team_name"] = match.get(
                    "blue_team" if self.settings["reader"] == "blue" else "gold_team")
                self.state["is_warmup"] = match.get("is_warmup", False)
                self.state["match_score"] = "{}-{}".format(
                    match.get("blue_score" if self.settings["reader"] == "blue" else "gold_score", 0),
                    match.get("gold_score" if self.settings["reader"] == "blue" else "blue_score", 0),
                )

            else:
                self.state["team_name"] = None
                self.state["match_score"] = None

            self.state["team_name_set"] = time.monotonic()

            return

        if message.get("type") == "gamestart" and int(message.get("cabinet_id")) == self.cabinet_id:
            self.state["gamestart"] = time.monotonic()
            self.state["game_running"] = True

        if message.get("type") == "gameend" and int(message.get("cabinet_id")) == self.cabinet_id:
            self.state["game_running"] = False

    def on_error(self):
        pass

    def on_close(self):
        pass

    def listen(self):
        logger.info("Starting gamestate thread.")

        while True:
            try:
                wsapp = websocket.WebSocketApp(
                    self.gamestate_url,
                    on_message=self.on_message,
                    on_error=self.on_error,
                    on_close=self.on_close,
                )

                logger.info("Gamestate connection online.")
                wsapp.run_forever(ping_interval=15, ping_timeout=5)

            except Exception as e:
                logger.exception("Exception in gamestate listener")

            time.sleep(1)
