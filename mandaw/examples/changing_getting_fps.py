from mandaw import *


mandaw = Mandaw(fps=120)

#or

mandaw.set_fps(60)

while True:
    print(mandaw.get_fps())
    mandaw.run()