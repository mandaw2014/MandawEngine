from mandaw import *
import random

# General Setup
mandaw = Mandaw("Pong")

bg_color = Color("black")
light_gray = (200, 200, 200)

class Paddle(GameObject):
    def __init__(self, x, y):
        super().__init__(
            window = mandaw,
            shape = "rect",
            width = 10,
            height = 140,
            x = x,
            y = y,
            color = light_gray
        )

        self.player_pos = mandaw.height / 2 - 70
        self.opponent_speed = 7

    def player_movement(self):
        self.y = self.player_pos

        if self.top <= 0:
            self.top = 0
        if self.bottom >= mandaw.height:
            self.bottom = mandaw.height

    def opponent_movement(self):
        if self.top < ball.y:
            self.top += self.opponent_speed
        if self.bottom > ball.y:
            self.bottom -= self.opponent_speed

        if self.top <= 0:
            self.top = 0
        if self.bottom >= mandaw.height:
            self.bottom = mandaw.height

class Ball(GameObject):
    def __init__(self):
        super().__init__(
            window = mandaw,
            shape = "ellipse",
            width = 20,
            height = 20,
            x = mandaw.width / 2 - 15,
            y = mandaw.height / 2 - 15,
            color = light_gray
        )

        self.ball_speed_x = 7 * random.choice((1, -1))
        self.ball_speed_y = 7 * random.choice((1, -1))

    def ball_movement(self):
        # Animate the ball
        self.x += self.ball_speed_x
        self.y += self.ball_speed_y

        # Collisions
        if self.top <= 0 or self.bottom >= mandaw.height:
            self.ball_speed_y *= -1
        if self.left <= 0 or self.right >= mandaw.width:
            self.ball_reset()

        if self.colliderect(player) or self.colliderect(opponent):
            self.ball_speed_x *= -1

    def ball_reset(self):
        self.center()
        self.ball_speed_y *= random.choice((1, -1))
        self.ball_speed_x *= random.choice((1, -1))

ball = Ball()
player = Paddle(mandaw.width - 20, mandaw.height / 2 - 70)
opponent = Paddle(10, mandaw.height / 2 - 70)

speed = 7

input = Input()

while True:
    # Handling inputs
    if mandaw.keys[input.UP]:
        player.player_pos -= speed

    if mandaw.keys[input.DOWN]:
        player.player_pos += speed

    # Ball movement
    ball.ball_movement()
    
    # Player movement
    player.player_movement()

    # Opponent movement
    opponent.opponent_movement()

    # Visuals
    mandaw.window.fill(bg_color)
    player.draw()
    opponent.draw()
    ball.draw()

    line = Line(mandaw, light_gray, (mandaw.width / 2, 0), (mandaw.width / 2, mandaw.height))

    mandaw.run()
