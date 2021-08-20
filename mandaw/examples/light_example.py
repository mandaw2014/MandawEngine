from mandaw import *


mandaw = Mandaw(bg_color="red")
light = Light(mandaw, "assets/circle.png")
light.light_init((100, 100))


while True:
    light.draw()
    mandaw.run()