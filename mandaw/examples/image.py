from mandaw import *
import os

mandaw = Mandaw()

path = os.path.dirname(os.path.abspath(__file__))
bird = os.path.join(path, "./assets/bird.jpeg")

image = Sprite(mandaw, bird, 0, 0)

width = image.get_width()
height = image.get_height()

print(width, height)

while True:
    image.draw()
    mandaw.run()