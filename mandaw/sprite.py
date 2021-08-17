import pygame

class Sprite:
    def __init__(self, window, image, x, y):
        self.image = pygame.image.load(image)
        self.window = window

        self.x = x
        self.y = y

    def draw(self):
        self.window.window.blit(self.image, (self.x, self.y))

    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()