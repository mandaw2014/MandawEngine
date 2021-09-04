import pygame

class Input:
    def __init__(self):
        self.pressed = pygame.key.get_pressed()
        self.mouse = pygame.mouse.get_pressed()

    def update(self):
        self.pressed = pygame.key.get_pressed()
        self.mouse = pygame.mouse.get_pressed()

    def get_key_pressed(self, key):
        return self.pressed[key]

    def get_mouse_button(self, button):
        return self.mouse[button]
