import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

#PIN ASSIGNMENTS

    #SW4 #SW5
    #SW1 #SW2 #SW3 <-- left to right, bottom to top

# Key Switches: Top to bottom, left to right
keyboard.pins = [
    board.D0,  # SW5, top
    board.D6, # SW1, left
    board.D5, # SW2, center
    board.D4, # SW3, right
]

# Encoder Pins: Phase A, Phase B, Push Switch (#SW4)
encoder_handler.pins = (
    (board.D2, board.D3, board.D1)
)

#MAPPINGS

keyboard.keymap = [
    [
        KC.LCMD(KC.C),   #SW5 top - copy
        KC.LCMD(KC.V),   #SW1 left - paste
        KC.LCMD(KC.X),   #SW2 center - cut
        KC.LCMD(KC.Z),   #SW3 right - undo
    ],
]

encoder_handler.map = [
    (
        #volume up, volume down, mute
        (KC.VOLU, KC.VOLD, KC.MUTE), 
    ),
]

if __name__ == '__main__':
    keyboard.go()