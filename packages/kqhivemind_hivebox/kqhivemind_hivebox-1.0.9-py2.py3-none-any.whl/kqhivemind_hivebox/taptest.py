import time

from .gpio import GPIO
from .lcddriver import LCD

settings = {
    "pin_config": [
        { "position": "queen", "button": 69, "light": 70 },
    ]
}

gpio = GPIO(settings)
lcd = LCD(port=2)
lcd.set_backlight(False)

state = {
    last_tap: None,
    tap_start: None,
    tap_count: 0,
}

def set_screen():
    if tap_start and last_tap and last_tap > time.monotonic() - 10:
        lcd.set_backlight(True)
        lcd.display_string("Tap Rate:")
        lcd.display_string("{6.02f} /sec".format(tap_count / (last_tap - tap_start)))
    else:
        lcd.display_string(" " * 16, 1)
        lcd.display_string(" " * 16, 2)
        lcd.set_backlight(False)

    time.sleep(0.5)

def button_pressed(button):
    if tap_start is None or last_tap < time.monotonic() - 10:
        tap_start = time.monotonic()
        tap_count = 0

    last_tap = time.monotonic()
    tap_count += 1

screen_thread = threading.Thread(target=set_screen, name="screen", daemon=True)
screen_thread.start()

gpio.on_button_press(button_pressed)
