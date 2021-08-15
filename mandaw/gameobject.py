import turtle

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