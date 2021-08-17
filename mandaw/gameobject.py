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
        pygame.draw.rect(self.window, self.color, self)

    def draw_ellipse(self):
        pygame.draw.ellipse(self.window, self.color, self)
        
if __name__ == '__main__':
    from mandaw import *

    mandaw = Mandaw()

    demo = GameObject(window = mandaw.window,
               width = 20,
               height = 20,
               x = mandaw.width / 2 - 15,
               y = mandaw.height / 2 - 15,
               color=white)

    while True:
        demo.draw_rect()
        mandaw.run()
