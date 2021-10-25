import pygame

class GameObject(pygame.Rect):
    def __init__(self, window, shape = "rect", width = 20, height = 20, x = 0, y = 0, color = "white"):
        self.shape = shape
        self.width = width
        self.height = height

        self.window = window
        self.color = color

        self.x = x
        self.y = y

        self.collider = "box"

    def draw(self):
        if self.shape == "rect" or self.shape == "rectangle" or self.shape == "square":
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
        try:
            if type(rect) != list:
                return self.colliderect(rect)
            elif type(rect) == list:
                return self.collidelistall(rect)
        except:
            raise AttributeError("MandawError: sorry but when you typed collide(object), the object wasnt a GameObject or a list of GameObjects. see you soon :)")

if __name__ == "__main__":
    from mandaw import *

    mandaw = Mandaw()

    demo = GameObject(mandaw, shape = "ellipse", width = 20, height = 20, x = 0, y = 0, color = "red")
    demo.center()

    @mandaw.draw
    def draw():
        demo.draw()
    
    mandaw.loop()
