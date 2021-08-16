import pygame

class GameObject(pygame.Rect):
    def __init__(self, window, x = 0, y = 0, color = "white", width = 20, height = 20):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.window = window
        self.color = color

    def draw_rect(self):
        pygame.draw.rect(self.window, self.color, self)

    def draw_ellipse(self):
        pygame.draw.ellipse(self.window, self.color, self)