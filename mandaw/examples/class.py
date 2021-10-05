from mandaw import *

mandaw = Mandaw("Classes!", 800, 600)

class Cube(GameObject):
    def __init__(self):
        super().__init__(
            window = mandaw,
            width = 20,
            height = 20,
            x = 0,
            y = 0,
            color = Color(0, 255, 255)
        )

        self.center()

cube = Cube()

while True:
    cube.draw()
    mandaw.run()