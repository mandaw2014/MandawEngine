import sdl2

class Input:
    def __init__(self):
        self.pressed = sdl2.SDL_GetKeyboardState(None)

        self.keys = {
            "UP":sdl2.SDL_SCANCODE_UP, "DOWN":sdl2.SDL_SCANCODE_DOWN,
            "LEFT":sdl2.SDL_SCANCODE_LEFT, "RIGHT":sdl2.SDL_SCANCODE_RIGHT,

            "A":sdl2.SDL_SCANCODE_A, "B":sdl2.SDL_SCANCODE_B, "C":sdl2.SDL_SCANCODE_C,
            "D":sdl2.SDL_SCANCODE_D, "E":sdl2.SDL_SCANCODE_E, "F":sdl2.SDL_SCANCODE_F,
            "G":sdl2.SDL_SCANCODE_G, "H":sdl2.SDL_SCANCODE_H, "I":sdl2.SDL_SCANCODE_I,
            "J":sdl2.SDL_SCANCODE_J, "K":sdl2.SDL_SCANCODE_K, "L":sdl2.SDL_SCANCODE_L,
            "M":sdl2.SDL_SCANCODE_M, "N":sdl2.SDL_SCANCODE_N, "O":sdl2.SDL_SCANCODE_O,
            "P":sdl2.SDL_SCANCODE_P, "Q":sdl2.SDL_SCANCODE_Q, "R":sdl2.SDL_SCANCODE_R,
            "S":sdl2.SDL_SCANCODE_S, "T":sdl2.SDL_SCANCODE_T, "U":sdl2.SDL_SCANCODE_U,
            "V":sdl2.SDL_SCANCODE_V, "W":sdl2.SDL_SCANCODE_W, "X":sdl2.SDL_SCANCODE_X,
            "Y":sdl2.SDL_SCANCODE_Y, "Z":sdl2.SDL_SCANCODE_Z,

            "0":sdl2.SDL_SCANCODE_0, "1":sdl2.SDL_SCANCODE_1,"2":sdl2.SDL_SCANCODE_2, 
            "3":sdl2.SDL_SCANCODE_3, "4":sdl2.SDL_SCANCODE_4, "5":sdl2.SDL_SCANCODE_5,
            "6":sdl2.SDL_SCANCODE_6, "7":sdl2.SDL_SCANCODE_7, "8":sdl2.SDL_SCANCODE_8,
            "9":sdl2.SDL_SCANCODE_9,

            "F1":sdl2.SDL_SCANCODE_F1, "F2":sdl2.SDL_SCANCODE_F2, "F3":sdl2.SDL_SCANCODE_F3,
            "F4":sdl2.SDL_SCANCODE_F4, "F5":sdl2.SDL_SCANCODE_F5, "F6":sdl2.SDL_SCANCODE_F6,
            "F7":sdl2.SDL_SCANCODE_F7, "F8":sdl2.SDL_SCANCODE_F8, "F9":sdl2.SDL_SCANCODE_F9,
            "F10":sdl2.SDL_SCANCODE_F10, "F11":sdl2.SDL_SCANCODE_F11, "F12":sdl2.SDL_SCANCODE_F12,
            "F13":sdl2.SDL_SCANCODE_F13, "F14":sdl2.SDL_SCANCODE_F14, "F15":sdl2.SDL_SCANCODE_F15,

            "LCTRL":sdl2.SDL_SCANCODE_LCTRL, "RCTRL":sdl2.SDL_SCANCODE_RCTRL,
            "LSHIFT":sdl2.SDL_SCANCODE_LSHIFT, "RSHIFT":sdl2.SDL_SCANCODE_RSHIFT,
            "LALT":sdl2.SDL_SCANCODE_LALT, "RALT":sdl2.SDL_SCANCODE_RALT,

            "HOME":sdl2.SDL_SCANCODE_HOME, "INSERT":sdl2.SDL_SCANCODE_INSERT,
            "DELETE":sdl2.SDL_SCANCODE_DELETE, "RETURN":sdl2.SDL_SCANCODE_RETURN,
            "SPACE":sdl2.SDL_SCANCODE_SPACE, "PLUS":sdl2.SDL_SCANCODE_KP_PLUS,
        }