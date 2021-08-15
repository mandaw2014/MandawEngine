import turtle
import os

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


class GameObject(turtle.Turtle):
    def __init__(self, shape = "square", color = "white", width = 1, height = 1, x = 0, y = 0):
        super().__init__()

        self.x = x
        self.y = y

        self.speed(0)
        self.shape(shape)
        self.color(color)
        self.shapesize(width, height)
        self.penup()
        self.goto(x, y)


class Text(turtle.Turtle):
    def __init__(self, text, align, font, x, y, color = "white"):
        super().__init__()

        align = "center"

        self.text = text
        self.x = x
        self.y = y
        self.colour = color
        self.align = align
        self.font = font

        self.speed(0)
        self.color(self.colour)
        self.penup()
        self.hideturtle()
        self.goto(self.x, self.y)
        self.write(self.text, align = self.align, font = self.font)

class Audio:
    def __init__(self, path):
        super().__init__()

        os.system("afplay " + path + "&")
