from mandaw import *
import random

mandaw = Mandaw("Pong", 800, 600)

BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)

class Paddle(GameObject):
    def __init__(self, x, y):
        super().__init__(
            mandaw,
            width = 20,
            height = 100,
            x = x,
            y = y,
            color = WHITE
        )

        self.ball = None

    def player_movement(self):
        if mandaw.input.pressed[mandaw.input.keys["UP"]]:
            self.y -= 2
        if mandaw.input.pressed[mandaw.input.keys["DOWN"]]:
            self.y += 2

        if self.y >= mandaw.height - 30:
            self.y = mandaw.height - 30
        if self.y <= -60:
            self.y = -60

    def opponent_movement(self):
        if self.y < self.ball.y:
            self.y += 2
        if self.y > self.ball.y:
            self.y -= 2

        if self.y >= mandaw.height - 30:
            self.y = mandaw.height - 30
        if self.y <= -60:
            self.y = -60

class Ball(GameObject):
    def __init__(self, x, y):
        super().__init__(
            mandaw,
            width = 20,
            height = 20,
            x = x,
            y = y,
            color = WHITE
        )

        self.ball_speed_x = 1 * random.choice((1, -1))
        self.ball_speed_y = 1 * random.choice((1, -1))

    def ball_movement(self):
        self.x += 2 * self.ball_speed_x
        self.y += 2 * self.ball_speed_y

        # Collisions
        if self.y <= 2 or self.y >= mandaw.height - 20:
            self.ball_speed_y *= -1
        if self.x <= 0:
            self.reset()
        elif self.x >= mandaw.width:
            self.reset()

    def reset(self):
        self.center()
        self.ball_speed_y *= random.choice((1, -1))
        self.ball_speed_x *= random.choice((1, -1))

player = Paddle(x = 0, y = 250)
player1 = Paddle(x = 780, y = 250)

ball = Ball(x = 390, y = 290)
ball.center()

player1.ball = ball

while True:
    player.player_movement()
    player1.opponent_movement()

    if ball.collide(player) or ball.collide(player1):
        ball.ball_speed_x *= -1

    ball.ball_movement()

    player.draw()
    player1.draw()
    ball.draw()
    mandaw.run()