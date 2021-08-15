import turtle

from mandaw.gameobject import GameObject
from mandaw.text import Text
from mandaw.audio import Audio

class Mandaw:
    def __init__(self, title, width, height, bgcolor):
        super().__init__()
        
        self.width = width
        self.height = height

        self.window = turtle.Screen()
        self.window.title(title)
        self.window.bgcolor(bgcolor)
        self.window.setup(width, height)
        self.window.tracer(0)
        self.window.listen()

        self.window.onkeypress(turtle.bye, "Escape")

    def run(self):
        self.window.update()
