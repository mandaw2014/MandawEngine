import pygame

class GameObject(pygame.Rect):
    def __init__(self, window, width = 20, height = 20, x = 0, y = 0, color = "white"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.window = window
        self.color = color

    def draw_rect(self):
        pygame.draw.rect(self.window.window, self.color, self)

    def draw_ellipse(self):
        pygame.draw.ellipse(self.window.window, self.color, self)
    
    def center(self):
        self.x = self.window.width / 2 - self.width / 2
        self.y = self.window.height / 2 - self.height / 2

if __name__ == "__main__":
    from mandaw import *

    mandaw = Mandaw()

    demo = GameObject(mandaw, width = 20, height = 20, x = 0, y = 0, color = "red")
    demo.center()

    while True:
        demo.draw_rect()
        mandaw.run()