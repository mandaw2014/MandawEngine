from mandaw import *
from pygame.math import Vector2

mandaw = Mandaw("Physics!")

player = GameObject(mandaw, "rect", (20, 20), 0, 0, "white")
player.center()

GRAVITY = 1.62

x = mandaw.width * 0.5
y = mandaw.height * 0.5

acceleration = Vector2(0, 0)
velocity = Vector2(0, 0)
position = Vector2(x, y)
gravity = Vector2(0, GRAVITY)

while True:
    move_left = mandaw.input.get_key_pressed(mandaw.keys["A"])
    move_right = mandaw.input.get_key_pressed(mandaw.keys["D"])
    move_up = mandaw.input.get_key_pressed(mandaw.keys["W"])
    move_down = mandaw.input.get_key_pressed(mandaw.keys["S"])

    acceleration.x = (move_right - move_left) * 0.5
    acceleration.y -= move_up
    acceleration.y += move_down

    velocity += acceleration * 0.5
    velocity += gravity * 0.1
    position += velocity + 0.5 * acceleration

    acceleration *= 0

    position.x = max(0, min(position.x, mandaw.width - player.width))
    position.y = max(0, min(position.y, mandaw.height - player.height))

    if position.y == mandaw.height - player.height:
        velocity.x *= 0.95

    player.x = position.x
    player.y = position.y

    player.draw()
    mandaw.run()