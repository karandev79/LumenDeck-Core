import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.media_keys import MediaKeys

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D0, board.D1, board.D2)
keyboard.row_pins = (board.D3, board.D4)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(MediaKeys())

encoder_handler = EncoderHandler()
encoder_handler.pins = (
    (board.D5, board.D6, board.D7),
)
encoder_handler.map = [
    (
        (KC.VOLD, KC.VOLU),
        (KC.MUTE, KC.MUTE),
    )
]
keyboard.modules.append(encoder_handler)

SNAP = KC.LGUI(KC.LSFT(KC.S))

keyboard.keymap = [
    [
        KC.COPY,  KC.PASTE,  KC.CUT,
        KC.UNDO,  KC.REDO,   SNAP,
    ]
]

if __name__ == '__main__':
    keyboard.go()