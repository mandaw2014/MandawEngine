from mandaw import *

mandaw = Mandaw("Mandaw", 800, 600)

square = GameObject(mandaw, width = 20, height = 20, color = Color(255, 0, 0))
square.center()

while True:
    square.draw()
    mandaw.run()