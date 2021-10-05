from mandaw import *

mandaw = Mandaw("Platformer!", width = 800, height = 600)
mandaw.bg_color = mandaw.color["cyan"]

objects = []

class PlatformerController2D(GameObject):
    def __init__(self, x = 0, y = 0, centered = True):
        super().__init__(
            mandaw,
            width = 15,
            height = 35,
            x = x,
            y = y,
            color = Color(255, 165, 0)
        )

        if centered == True:
            self.center()
        else:
            pass

        # Player's X Position
        self.pos_x = 0

        # Set the position as a variable
        self.pos = self.window.width / 2 - 15

        self.is_jumping = False
        self.jump_y = 5

        self.direction = None

        self.velocity_y = 1

        # Player's speed and maxspeed
        self.speed = 0.1
        self.maxspeed = 2

        self.ignore_speed = []

    def movement(self):
        # Player movement
        if mandaw.input.pressed[mandaw.input.keys["A"]]:
            self.pos_x -= self.speed * mandaw.dt
            self.direction = 0

        if mandaw.input.pressed[mandaw.input.keys["D"]]:
            self.pos_x += self.speed * mandaw.dt
            self.direction = 1

        # Momentum
        if self.pos_x >= self.maxspeed:
            self.pos_x = self.maxspeed
        if self.pos_x <= -self.maxspeed:
            self.pos_x = -self.maxspeed

        self.pos += int(self.pos_x)

        # Gravity
        if not self.collidelist(objects) and self.is_jumping == False:
            self.y += 3 * int(self.velocity_y)
            self.velocity_y += 0.1

        if self.collidelist(objects):
            self.velocity_y = 1

            if self.direction == 0 and not mandaw.input.pressed[mandaw.input.keys["A"]]:
                self.pos_x += 10

                if self.pos_x >= 0:
                    self.pos_x = 0
            
            if self.direction == 1 and not mandaw.input.pressed[mandaw.input.keys["D"]]:
                self.pos_x -= 10

                if self.pos_x <= 0:
                    self.pos_x = 0

        if not self.collidelist(objects):
            if self.direction == 0 and not mandaw.input.pressed[mandaw.input.keys["A"]]:
                self.pos_x += 0.1 * mandaw.dt

                if self.pos_x >= 0:
                    self.pos_x = 0
            
            if self.direction == 1 and not mandaw.input.pressed[mandaw.input.keys["D"]]:
                self.pos_x -= 0.1 * mandaw.dt

                if self.pos_x <= 0:
                    self.pos_x = 0

        # Set the x position as the x variable
        self.x = int(self.pos)

        self.jump()

    def jump(self):
        # Jumping
        if self.is_jumping == False and mandaw.input.pressed[mandaw.input.keys["SPACE"]]:
            self.is_jumping = True
            if not self.collidelist(objects):
                self.is_jumping = False

        if self.is_jumping == True:
            self.y -= self.jump_y
            self.jump_y -= 1

            if self.jump_y < -5:
                self.is_jumping = False
                self.jump_y = 10

class Platform(GameObject):
    def __init__(self, x, y):
        super().__init__(
            mandaw,
            width = 50,
            height = 10,
            x = x,
            y = y,
            color = Color(255, 255, 0)
        )

player = PlatformerController2D(0, 0, True)

ground = GameObject(mandaw, 5000, 100, 0, 500, color = Color(195, 195, 195))
ground.center_x()

platform = Platform(0, 450)
platform.center_x()

objects.append(platform)
objects.append(platform)

while True:
    platform.draw()
    player.draw()
    ground.draw()

    player.movement()

    mandaw.run()