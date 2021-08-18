import pygame

class Text:
    def __init__(self, window, text, font_size = 24, style = None, color = "white", x = 0, y = 0):
        self.window = window
        self.font_size = font_size
        self.style = style
        self.font = pygame.font.SysFont(self.style, self.font_size)
        self.color = color
        self.x = x
        self.y = y

        self.text = self.font.render(text, True, self.color)

    def draw(self):
        self.window.window.blit(self.text, (self.x, self.y))

    def center(self):
        self.x = self.window.width / 2 - self.font_size / 2
        self.y = self.window.height / 2 - self.font_size / 2
