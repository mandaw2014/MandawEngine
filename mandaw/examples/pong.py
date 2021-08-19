from mandaw import *
import random

# General Setup
mandaw = Mandaw("Pong")

bg_color = Color("black")
light_gray = (200, 200, 200)

score1 = 0
score2 = 0

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
        global score1
        global score2
        # Animate the ball
        self.x += 70 * self.ball_speed_x * mandaw.dt
        self.y += 70 * self.ball_speed_y * mandaw.dt

        # Collisions
        if self.top <= 0 or self.bottom >= mandaw.height:
            self.ball_speed_y *= -1
        if self.left <= 0:
            self.ball_reset()
            score2 += 1
        elif self.right >= mandaw.width:
            self.ball_reset()
            score1 += 1

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

while True:
    # Handling inputs
    if mandaw.controls.is_key_pressed(mandaw.keys["UP"]):
        player.player_pos -= 100 * speed * mandaw.dt

    if mandaw.controls.is_key_pressed(mandaw.keys["DOWN"]):
        player.player_pos += 100 * speed * mandaw.dt

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
    score1_text = Text(mandaw, str(score1), 24, None, "white", 10)
    score2_text = Text(mandaw, str(score2), 24, None, "white", mandaw.width - 20)
    score1_text.draw()
    score2_text.draw()


    line = Line(mandaw, light_gray, (mandaw.width / 2, 0), (mandaw.width / 2, mandaw.height))

    mandaw.run()
