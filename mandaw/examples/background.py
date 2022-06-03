from mandaw import *

mandaw = Mandaw("Mountain Background", 800, 600, "white")

mandaw.background = Sprite(mandaw, "./assets/mountains.png", 0, 0, width = mandaw.width, height = mandaw.height)

mandaw.loop()