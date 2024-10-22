import math
import threading
import time
from enum import Enum

import gpiod
from gpiod.edge_event import EdgeEvent
from gpiod.line import Bias, Direction, Edge, Value

from .util import get_position_id


class GPIO:
    def __init__(self, settings=None):
        self.settings = settings or {}
        self.buttons = {}
        self.button_down_time = {}
        self.button_press_time = {}
        self.lights = {}
        self.brightness = {}
        self.gpiod_config = {}
        self.max_brightness = 1

        self.pwm_freq = 0.1
        self.pwm_poll_freq = 1

        self.blink_rate = 0.50
        self.pulse_rate = 0.75

        self.button_hold_time = 1.00
        self.button_debounce_time = 0.5

        for player in settings.get("pin_config", {}):
            if "light" in player:
                self.lights[get_position_id(player, settings["reader"])] = player["light"]
                self.brightness[player["light"]] = 0

            if "button" in player:
                self.buttons[get_position_id(player, settings["reader"])] = player["button"]

        self.button_thread = threading.Thread(target=self.listen_buttons, name="buttons", daemon=True)
        self.button_thread.start()

        self.light_threads = [
            threading.Thread(target=self.set_lights, name="lights{}".format(pin), args=[pin], daemon=True)
            for pin in self.lights.values()
        ]

        for light_thread in self.light_threads:
            light_thread.start()

        self._on_button_press = []
        self._on_button_release = []
        self._on_button_hold = []

    def on_button_press(self, fn):
        self._on_button_press.append(fn)

    def button_press(self, button):
        for fn in self._on_button_press:
            fn(button)

    def on_button_release(self, fn):
        self._on_button_release.append(fn)

    def button_release(self, button):
        for fn in self._on_button_release:
            fn(button)

    def on_button_hold(self, fn):
        self._on_button_hold.append(fn)

    def button_hold(self, button):
        for fn in self._on_button_hold:
            fn(button)

    def button_request(self):
        gpiod_config = {
            pin: gpiod.LineSettings(
                direction=Direction.INPUT, edge_detection=Edge.BOTH, bias=Bias.PULL_DOWN,
            )
            for pin in self.buttons.values()
        }

        return gpiod.request_lines(
            self.settings.get("gpio_device", "/dev/gpiochip0"),
            consumer="hivemind-nfc-buttons",
            config=gpiod_config,
        )

    def listen_buttons(self):
        if len(self.buttons) == 0:
            return

        with self.button_request() as request:
            while True:
                for event in request.read_edge_events():
                    pin = event.line_offset

                    if event.event_type == EdgeEvent.Type.RISING_EDGE:
                        self.button_down_time[pin] = time.monotonic()

                    if event.event_type == EdgeEvent.Type.FALLING_EDGE:
                        if self.button_press_time.get(pin, 0) < time.monotonic() - self.button_debounce_time:
                            self.button_release(pin)

                            if time.monotonic() > self.button_down_time.get(pin, 0) + self.button_hold_time:
                                self.button_hold(pin)
                            else:
                                self.button_press(pin)

                            self.button_press_time[pin] = time.monotonic()

                        self.button_down_time.pop(pin, None)

    def set_lights(self, pin):
        gpiod_config = {
            pin: gpiod.LineSettings(
                direction=Direction.OUTPUT, output_value=Value.INACTIVE,
            )
        }

        with gpiod.request_lines(
            self.settings.get("gpio_device", "/dev/gpiochip0"),
            consumer="hivemind-nfc-lights",
            config=gpiod_config,
        ) as request:
            while True:
                brightness = self.brightness[pin] * self.max_brightness
                if brightness:
                    for _ in range(self.pwm_poll_freq):
                        if brightness > 0.5:
                            request.set_value(pin, Value.ACTIVE)
                        else:
                            request.set_value(pin, Value.INACTIVE)

                        time.sleep(self.pwm_freq * self.pwm_poll_freq)
                else:
                    request.set_value(pin, Value.INACTIVE)
                    time.sleep(self.pwm_freq * self.pwm_poll_freq)
