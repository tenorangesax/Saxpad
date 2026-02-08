import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.scanners.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC

keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())

PINS = [board.D1, board.D2, board.D3, board.D4]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

encoder = EncoderHandler()
keyboard.modules.append(encoder)

encoder.pins = (
    (board.D5, board.D6),  # encoder A/B pins
)

keyboard.keymap = [
    # Layer 0 — Base (Copy / Paste)
    [
        KC.LGUI(KC.C),     # Copy
        KC.LGUI(KC.V),     # Paste
        KC.LGUI(KC.TAB),   # App switch
        KC.LGUI(KC.W),     # Close tab
    ],

    # Layer 1 — (Keys can be anything or NOOP)
    [
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
    ],

    # Layer 2 — Optional extra layer
    [
        KC.LEFT,
        KC.DOWN,
        KC.UP,
        KC.RIGHT,
    ],
]

encoder.map = [

    (
        KC.VOLD,      # Rotate left
        KC.VOLU,      # Rotate right
        KC.TO(1),     # Press → go to Layer Select Mode
    ),

    (
        KC.TO(0),     # Rotate left → Base layer
        KC.TO(2),     # Rotate right → Nav layer
        KC.TO(0),     # Press → Back to base + volume control
    ),


    (
        KC.VOLD,
        KC.VOLU,
        KC.TO(0),
    ),
]

if __name__ == '__main__':
    keyboard.go()
