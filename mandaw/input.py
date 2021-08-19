import pygame

class Controls:
    def __init__(self):
        self.pressed = pygame.key.get_pressed()

    def update(self):
        self.pressed = pygame.key.get_pressed()

    def is_key_pressed(self, key):
        return self.pressed[key]
