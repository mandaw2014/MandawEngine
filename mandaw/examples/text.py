from mandaw import *

mandaw = Mandaw("Mandaw", bg_color = "cyan")

text = Text(mandaw, "Mandaw", 50)
text.center()

while True:
    text.draw()
    mandaw.run()