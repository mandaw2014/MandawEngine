from mandaw.main import *

mandaw = Mandaw("Platformer", 800, 600, "cyan")

class PlaformerController(GameObject):
    def __init__(self, x, y):
        super().__init__(
            shape = "square",
            color = "orange",
            width = 4,
            height = 2,
            x = x,
            y = y
        )

        self.x = x
        self.y = y

        mandaw.window.onkeypress(self.move_left, "a")
        mandaw.window.onkeypress(self.move_right, "d")
        mandaw.window.onkeypress(self.jump, "space")

    def move_right(self):
        if not self.x > 370:
            self.x += 10
            self.setx(self.x)

    def move_left(self):
        if not self.x < -370:
            self.x -= 10
            self.setx(self.x)

    def jump(self):
        if self.y <= -60:
            self.y += 100
            self.sety(self.y)

player = PlaformerController(0, 0)

ground = GameObject(shape = "square", color = "gray", width = 10, height = 200, x = 0, y = -200)

while True:
    if not player.y < -60:
        player.y -= 5
        player.sety(player.y)

    mandaw.run()