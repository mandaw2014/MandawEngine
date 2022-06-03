from mandaw import *
from pygame.math import Vector2

mandaw = Mandaw("Physics!")

player = GameObject(mandaw, "rect", 20, 20, 0, 0, "white")
player.center()

GRAVITY = 1.62

x = mandaw.width * 0.5
y = mandaw.height * 0.5

acceleration = Vector2(0, 0)
velocity = Vector2(0, 0)
position = Vector2(x, y)
gravity = Vector2(0, GRAVITY)

@mandaw.update
def update(dt):
    global acceleration, velocity, position
    move_left = mandaw.input.get_key_pressed(mandaw.input.keys["A"])
    move_right = mandaw.input.get_key_pressed(mandaw.input.keys["D"])
    move_up = mandaw.input.get_key_pressed(mandaw.input.keys["W"])
    move_down = mandaw.input.get_key_pressed(mandaw.input.keys["S"])

    acceleration.x = (move_right - move_left) * 30 * dt
    acceleration.y -= move_up * 30 * dt
    acceleration.y += move_down * 30 * dt

    velocity += acceleration * 30 * dt
    velocity += gravity * 30 * dt
    position += velocity + 30 * acceleration * dt

    acceleration *= 0

    position.x = max(0, min(position.x, mandaw.width - player.width))
    position.y = max(0, min(position.y, mandaw.height - player.height))

    if position.y == mandaw.height - player.height:
        velocity.x *= 0.95

    player.x = position.x
    player.y = position.y

@mandaw.draw
def draw():
    player.draw()

mandaw.loop()