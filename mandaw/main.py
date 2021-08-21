import time
import pygame
from mandaw.input import Controls

class Mandaw:
    def __init__(self, title = "Mandaw", width = 800, height = 600, bg_color = "black"):
        self.width = width
        self.height = height
        self.title = title
        self.bg_color = bg_color
        self.fps = 60
        self.done = False

        pygame.init()
        self.clock = pygame.time.Clock()

        self.last_time = time.time()
        self.dt = 0

        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.window.fill(self.bg_color)

        self.controls = Controls()

        self.keys = {
            "UP":pygame.K_UP, "DOWN":pygame.K_DOWN,
            "LEFT":pygame.K_LEFT, "RIGHT":pygame.K_RIGHT,

            "A":pygame.K_a, "B":pygame.K_b, "C":pygame.K_c,
            "D":pygame.K_d, "E":pygame.K_e, "F":pygame.K_f,
            "G":pygame.K_g, "H":pygame.K_h, "I":pygame.K_i,
            "J":pygame.K_j, "K":pygame.K_k, "L":pygame.K_l,
            "M":pygame.K_m, "N":pygame.K_n, "O":pygame.K_o,
            "P":pygame.K_p, "Q":pygame.K_q, "R":pygame.K_r,
            "S":pygame.K_s, "T":pygame.K_t, "U":pygame.K_u,
            "V":pygame.K_v, "W":pygame.K_w, "X":pygame.K_x,
            "Y":pygame.K_y, "Z":pygame.K_z,

            "0":pygame.K_0, "1":pygame.K_1,"2":pygame.K_2, 
            "3":pygame.K_3, "4":pygame.K_4, "5":pygame.K_5,
            "6":pygame.K_6, "7":pygame.K_7, "8":pygame.K_8,
            "9":pygame.K_9,

            "F1":pygame.K_F1, "F2":pygame.K_F2, "F3":pygame.K_F3,
            "F4":pygame.K_F4, "F5":pygame.K_F5, "F6":pygame.K_F6,
            "F7":pygame.K_F7, "F8":pygame.K_F8, "F9":pygame.K_F9,
            "F10":pygame.K_F10, "F11":pygame.K_F11, "F12":pygame.K_F12,
            "F13":pygame.K_F13, "F14":pygame.K_F14, "F15":pygame.K_F15,

            "SCAN_F1":pygame.KSCAN_F1, "SCAN_F2":pygame.KSCAN_F2, 
            "SCAN_F3":pygame.KSCAN_F3, "SCAN_F4":pygame.KSCAN_F4, 
            "SCAN_F5":pygame.KSCAN_F5, "SCAN_F6":pygame.KSCAN_F6,
            "SCAN_F7":pygame.KSCAN_F7, "SCAN_F8":pygame.KSCAN_F8, 
            "SCAN_F9":pygame.KSCAN_F9, "SCAN_F10":pygame.KSCAN_F10, 
            "SCAN_F11":pygame.KSCAN_F11, "SCAN_F12":pygame.KSCAN_F12,
            "SCAN_F13":pygame.KSCAN_F13, "SCAN_F14":pygame.KSCAN_F14, 
            "SCAN_F15":pygame.KSCAN_F15,

            "LCTRL":pygame.K_LCTRL, "RCTRL":pygame.K_RCTRL,
            "LSHIFT":pygame.K_LSHIFT, "RSHIFT":pygame.K_RSHIFT,
            "LALT":pygame.K_LALT, "RALT":pygame.K_RALT,
            "LSUPER":pygame.K_LSUPER, "RSUPER":pygame.K_RSUPER,

            "MOD_CTRL":pygame.KMOD_CTRL, "MOD_ALT":pygame.KMOD_ALT,
            "MOD_CAPS":pygame.KMOD_CAPS, "MOD_GUI":pygame.KMOD_GUI,
            "MOD_LALT":pygame.KMOD_LALT, "MOD_LCTRL":pygame.KMOD_LCTRL,
            "MOD_LGUI":pygame.KMOD_LGUI, "MOD_LMETA":pygame.KMOD_LMETA,
            "MOD_LSHIFT":pygame.KMOD_LSHIFT, "MOD_META":pygame.KMOD_META,
            "MOD_NONE":pygame.KMOD_NONE, "MOD_MODE":pygame.KMOD_MODE,
            "MOD_NUM":pygame.KMOD_NUM, "MOD_RALT":pygame.KMOD_RALT,
            "MOD_RSHIFT":pygame.KMOD_RSHIFT, "MOD_RCTRL":pygame.KMOD_RCTRL,
            "MOD_RMETA":pygame.KMOD_RMETA, "MOD_RGUI":pygame.KMOD_RGUI,
            "MOD_SHIFT":pygame.KMOD_SHIFT, "MODE":pygame.K_MODE,
            "SCAN_MODE":pygame.KSCAN_MODE,

            "HOME":pygame.K_HOME, "INSERT":pygame.K_INSERT,
            "DELETE":pygame.K_DELETE, "RETURN":pygame.K_RETURN,
            "SPACE":pygame.K_SPACE, "PLUS":pygame.K_PLUS
        }

    def run(self):
        pygame.display.flip()
        self.clock.tick(60)

        pygame.display.update()

        self.dt = time.time() - self.last_time
        self.dt *= 60
        self.last_time = time.time()

        self.controls.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
                pygame.quit()
                quit()

        self.window.fill(self.bg_color)
