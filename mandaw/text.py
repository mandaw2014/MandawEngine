import pygame
from sys import platform

class Text:
    def __init__(self, window, text, font_size = 24, file = None, color = "white", x = 0, y = 0):
        self.window = window
        self.font_size = font_size
        self.file = file

        if platform == "linux" or platform == "linux2":
            self.font = pygame.font.SysFont(self.file, self.font_size)
        if platform == "darwin":
            self.font = pygame.font.Font(self.file, self.font_size)
        if platform == "win32":
            self.font = pygame.font.SysFont(self.file, self.font_size)

        self.color = color
        self.x = x
        self.y = y

        self.text = self.font.render(text, True, self.color)

    def draw(self):
        self.window.window.blit(self.text, (self.x, self.y))

    def center(self):
        self.x = self.window.width / 2 - self.font_size / 2
        self.y = self.window.height / 2 - self.font_size / 2

if __name__ == '__main__':
    from mandaw import *

    mandaw = Mandaw("Mandaw", bg_color="cyan")

    text = Text(mandaw, "Mandaw", 50)
    text.center()

    while True:
        text.draw()
        mandaw.run()
