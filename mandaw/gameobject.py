import pygame

class GameObject(pygame.Rect):
    def __init__(self, window, shape = "rect", width = 20, height = 20, x = 0, y = 0, color = "white"):
        self.x = x
        self.y = y
        self.shape = shape
        self.width = width
        self.height = height

        self.window = window
        self.color = color

    def draw(self):
        if self.shape == "rect" or self.shape == "rectangle":
            pygame.draw.rect(self.window.window, self.color, self)
        
        elif self.shape == "ellipse" or self.shape == "circle":
            pygame.draw.ellipse(self.window.window, self.color, self)
    
    def center(self):
        self.x = self.window.width / 2 - self.width / 2
        self.y = self.window.height / 2 - self.height / 2
    
    def center_x(self):
        self.x = self.window.width / 2 - self.width / 2

    def center_y(self):
        self.y = self.window.height / 2 - self.height / 2

    def collide(self, rect):
        if type(rect) != list:
            return self.colliderect(rect)
        elif type(rect) == list:
            return self.collidelistall(rect)
        else:
            print("MandawError: sorry but when you typed collide(object), the object wasnt a string or a list. see you soon :)")

if __name__ == "__main__":
    from mandaw import *

    mandaw = Mandaw()

    demo = GameObject(mandaw, shape = "ellipse", width = 20, height = 20, x = 0, y = 0, color = "red")
    demo.center()

    while True:
        demo.draw()
        mandaw.run()
