import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeycodes
from kmk.scanners import EncoderScanner

keyboard = KMKKeyboard()

encoder_pins = ((board.GP14, board.GP15, False),)

encoder_handler = EncoderHandler()
encoder_handler.pins = encoder_pins
encoder_handler.map = (((KC.VOLD, KC.VOLU, KC.MUTE),),)

keyboard.modules.append(encoder_handler)
keyboard.extensions.append(MediaKeycodes())
keyboard.scanners.append(EncoderScanner(encoder_handler))

keyboard.matrix = [
    [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11],
    [board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP23],
    [board.GP24, board.GP25, board.GP26, board.GP27, board.GP28, board.GP29, board.GP30, board.GP31, board.GP32, board.GP33, board.GP34, board.GP35],
    [board.GP36, board.GP37, board.GP38, board.GP39, board.GP40, board.GP41, board.GP42, board.GP43, board.GP44, board.GP45, board.GP46, board.GP47],
    [board.GP48, board.GP49, board.GP50, board.GP51, board.GP52, board.GP53, board.GP54, board.GP55, board.GP56, board.GP57, board.GP58, board.GP59],
    [board.GP60, board.GP61, board.GP62, board.GP63, board.GP64, board.GP65, board.GP66, board.GP67, board.GP68, board.GP69, board.GP70, board.GP71],
    [board.GP72, board.GP73, board.GP74, board.GP75, board.GP76, board.GP77, board.GP78, board.GP79, board.GP80, board.GP81, board.GP82, board.GP83],
    [board.GP84, board.GP85, board.GP86, board.GP87, board.GP88, board.GP89, board.GP90, board.GP91, board.GP92, board.GP93, board.GP94, board.GP95],
    [board.GP96, board.GP97, board.GP98, board.GP99, board.GP100, board.GP101, board.GP102, board.GP103, board.GP104, board.GP105, board.GP106, board.GP107],
]

keyboard.keymap = [
    [KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11],
    [KC.F12, KC.PSCR, KC.SLCK, KC.PAUS, KC.GRV, KC.1, KC.2, KC.3, KC.4, KC.5, KC.6, KC.7],
    [KC.8, KC.9, KC.0, KC.MINS, KC.EQL, KC.BSPC, KC.INS, KC.HOME, KC.PGUP, KC.TAB, KC.Q, KC.W],
    [KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.DEL],
    [KC.END, KC.PGDN, KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L],
    [KC.SCLN, KC.QUOT, KC.ENT, KC.LSFT, KC.NUBS, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M],
    [KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.UP, KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.RALT, KC.RGUI, KC.APP],
    [KC.RCTL, KC.LEFT, KC.DOWN, KC.RIGHT, KC.NLCK, KC.PSLH, KC.PAST, KC.PMNS, KC.P7, KC.P8, KC.P9, KC.PPLS],
    [KC.P4, KC.P5, KC.P6, KC.P1, KC.P2, KC.P3, KC.PENT, KC.P0, KC.PDOT, KC.NO, KC.NO, KC.NO],
]

if __name__ == "__main__":
    keyboard.go()
