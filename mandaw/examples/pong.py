from mandaw import *
import random

# General Setup
mandaw = Mandaw()

bg_color = Color("black")
light_gray = (200, 200, 200)

ball = GameObject(mandaw.window, mandaw.width / 2 - 15, mandaw.height / 2 - 15, light_gray, 20, 20)
player = GameObject(mandaw.window, mandaw.width - 20, mandaw.height / 2 - 70, light_gray, 10, 140) 
opponent = GameObject(mandaw.window, 10, mandaw.height / 2 - 70, light_gray, 10, 140)

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_pos = mandaw.height / 2 - 70
opponent_speed = 7

speed = 7

def ball_movement():
    global ball_speed_x, ball_speed_y
    # Animate the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Collisions
    if ball.top <= 0 or ball.bottom >= mandaw.height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= mandaw.width:
        ball_reset()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_movement():
    player.y = player_pos

    if player.top <= 0:
        player.top = 0
    if player.bottom >= mandaw.height:
        player.bottom = mandaw.height

def opponent_movement():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= mandaw.height:
        opponent.bottom = mandaw.height

def ball_reset():
    global ball_speed_x, ball_speed_y
    ball.center = (mandaw.width / 2, mandaw.height / 2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

while True:
    # Handling inputs
    if mandaw.keys[mandaw.UP]:
        player_pos -= speed

    if mandaw.keys[mandaw.DOWN]:
        player_pos += speed

    # Ball movement
    ball_movement()
    
    # Player movement
    player_movement()

    # Opponent movement
    opponent_movement()

    # Visuals
    mandaw.window.fill(bg_color)
    player.draw_rect()
    opponent.draw_rect()
    ball.draw_ellipse()

    line = Line(mandaw.window, light_gray, (mandaw.width / 2, 0), (mandaw.width / 2, mandaw.height))

    mandaw.run()