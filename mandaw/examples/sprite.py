from mandaw import *

mandaw = Mandaw("Sprites!", 800, 600)

sprite = Sprite(mandaw, "./mandaw/assets/mandaw.png")

while True:
    sprite.draw()
    mandaw.run()