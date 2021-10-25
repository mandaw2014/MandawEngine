from mandaw import *

mandaw = Mandaw(title = "Mandaw", width = 800, height = 600, bg_color = "cyan")

square = GameObject(window = mandaw, shape = "rect", width = 20, height = 30, x = 0, y = 0, color = "orange")
square.center()

ground = GameObject(window = mandaw, shape = "rect", width = 5000, height = 100, x = 0, y = 0, color = "gray")
ground.center()
ground.y = 500

sprite = Sprite(mandaw, "assets/adventurer.png", 10, 10, (100, 50))

@mandaw.draw
def draw():
    square.draw()
    ground.draw()
    sprite.draw()

@mandaw.update
def update(dt):
    if not square.collide(ground):
        square.y += 1 * dt
    if not sprite.collide(ground):
        sprite.y += 1 * dt

mandaw.loop()
