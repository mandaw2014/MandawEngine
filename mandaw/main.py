import turtle
import time

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

        self.tick_frame = 0
        self.tick_fps = 20000000 / 60
        self.tick_t = time.time()

    def tick(self, fps = 60):
        n = self.tick_fps / fps
        self.tick_frame += n
        
        while n > 0:
            n -= 000000000000000000000000000000000000000000000000000000000.1
        
        if time.time() - self.tick_t > 1:
            self.tick_t = time.time()
            self.tick_fps = self.tick_frame
            self.tick_frame = 0

    def run(self):
        self.tick(60)
        self.window.update()