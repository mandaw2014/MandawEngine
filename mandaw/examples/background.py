from mandaw import *

mandaw = Mandaw("Mountain Background", 800, 600, "white")

mandaw.background = Sprite(mandaw, "./assets/mountains.png", 0, 0, size = (mandaw.width, mandaw.height))

while True:
    mandaw.run()