print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP0,board.GP1,board.GP2,board.GP3,board.GP4,board.GP5,board.GP6,board.GP7,board.GP8,board.GP9,board.GP10,board.GP11,board.GP12,board.GP13,board.GP14)
keyboard.row_pins = (board.GP15,board.GP16,board.GP17,board.GP18,board.GP19,board.GP20)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# By default use AZERTY AFNOR layout
keyboard.keymap = [
    [KC.ESCAPE,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,KC.F6,KC.F7,KC.F8,KC.F9,KC.F10,KC.F11,KC.F12,KC.PSCREEN,KC.DELETE],
]

if __name__ == '__main__':
    keyboard.go()
