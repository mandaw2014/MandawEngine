import turtle

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