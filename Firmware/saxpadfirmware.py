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
    (board.D5, board.D6),  
)

keyboard.keymap = [
    
    [
        KC.LGUI(KC.C),    
        KC.LGUI(KC.V),     
        KC.LGUI(KC.TAB),   
        KC.LGUI(KC.W),    
    ],

    
    [
        KC.NO,
        KC.NO,
        KC.NO,
        KC.NO,
    ],

   
    [
        KC.LEFT,
        KC.DOWN,
        KC.UP,
        KC.RIGHT,
    ],
]

encoder.map = [

    (
        KC.VOLD,     
        KC.VOLU,      
        KC.TO(1),     
    ),

    (
        KC.TO(0),     
        KC.TO(2),     
        KC.TO(0),     
    ),


    (
        KC.VOLD,
        KC.VOLU,
        KC.TO(0),
    ),
]

if __name__ == '__main__':
    keyboard.go()
