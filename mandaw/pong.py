from mandaw import *

# Window
mandaw = Mandaw("Pong", 800, 600, "black")

# Score
score_a = 0
score_b = 0

class Paddle(GameObject):
    def __init__(self, x, y):
        super().__init__(
            shape = "square",
            color = "white",
            width = 5,
            height = 1,
            x = x,
            y = y
        )

    def paddle_up(self):
        y = self.ycor()
        if not y > 290:
            y += 20
            self.sety(y)

    def paddle_down(self):
        y = self.ycor()
        if not y < -290:
            y -= 20
            self.sety(y)

class Ball(GameObject):
    def __init__(self, x, y):
        super().__init__(
            shape = "circle",
            color = "white",
            width = 1,
            height = 1,
            x = x,
            y = y
        )
        
        self.dx = 0.2
        self.dy = 0.2

# Paddle A
paddle_a = Paddle(x = -350, y = 0)

# Paddle B
paddle_b = Paddle(x = 350, y = 0)

# Ball
ball = Ball(x = 0, y = 0)

# Score Text
score = Text(text = "Player A: 0  Player B: 0", align = "center", font = ("Courier", 24, "normal"), x = 0, y = 260)

mandaw.window.onkeypress(paddle_a.paddle_up, "w")
mandaw.window.onkeypress(paddle_a.paddle_down, "s")

mandaw.window.onkeypress(paddle_b.paddle_up, "Up")
mandaw.window.onkeypress(paddle_b.paddle_down, "Down")

# Main Game Loop
while True:
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > mandaw.height / 2 - 10:
        ball.sety(mandaw.height / 2 - 10)
        ball.dy *= -1

    if ball.ycor() < -mandaw.height / 2 + 20:
        ball.sety(-mandaw.height / 2 + 20)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        score.clear()
        score.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        score.clear()
        score.write("Player A: {}  Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    mandaw.run()
