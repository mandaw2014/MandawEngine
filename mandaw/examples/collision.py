from mandaw import *

mandaw = Mandaw("Collisions!", 800, 600)

player = GameObject(mandaw, 30, 30, 0, 0)
player.center()

objects = []

class CollisionObject(GameObject):
    def __init__(self, x, y):
        super().__init__(
            mandaw,
            width = 25,
            height = 25,
            x = x,
            y = y
        )

object1 = CollisionObject(600, 300)
object2 = CollisionObject(200, 300)
object3 = CollisionObject(400, 100)
object4 = CollisionObject(400, 400)

objects.append(object1)
objects.append(object2)
objects.append(object3)
objects.append(object4)

n = 1

while True:
    if mandaw.input.pressed[mandaw.input.keys["UP"]]:
        player.y -= 1 * mandaw.dt
    if mandaw.input.pressed[mandaw.input.keys["LEFT"]]:
        player.x -= 1 * mandaw.dt
    if mandaw.input.pressed[mandaw.input.keys["DOWN"]]:
        player.y += 1 * mandaw.dt
    if mandaw.input.pressed[mandaw.input.keys["RIGHT"]]:
        player.x += 1 * mandaw.dt
      
    if mandaw.input.pressed[mandaw.input.keys["G"]]:
        player.center()

    if player.collidelist(objects):
        print("Hit! " + str(n))
        n += 1

    object1.draw()
    object2.draw()
    object3.draw()
    object4.draw()

    player.draw()

    mandaw.run()