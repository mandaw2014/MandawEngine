from mandaw import *

# Window
mandaw = Mandaw("Platformer", bg_color = "cyan")

# Ground
ground = GameObject(mandaw, shape = "rect", width = 5000, height = 100, x = mandaw.width / 2 - 500, y = 500, color = "gray")

# Objects list
objects = []

# Player
class PlatformerController(GameObject):
    def __init__(self):
        super().__init__(
            window = mandaw,
            shape = "rect",
            width = 15,
            height = 35,
            color = "orange",
        )

        self.center()
        self.y = mandaw.height / 2 + 150
        
        # Player's X Position
        self.pos_x = 0

        # Set the position as a variable
        self.pos = mandaw.width / 2 - self.width

        self.is_jumping = False
        self.jump_y = 10

        self.direction = None

        self.velocity_y = 1

        # Player's speed and maxspeed
        self.speed = 50
        self.maxspeed = 5

    def movement(self):
        # Player movement
        if mandaw.controls.is_key_pressed(mandaw.keys["A"]):
            self.pos_x -= self.speed * mandaw.dt
            self.direction = 0

        if mandaw.controls.is_key_pressed(mandaw.keys["D"]):
            self.pos_x += self.speed * mandaw.dt
            self.direction = 1

        # Momentum
        if self.pos_x >= self.maxspeed:
            self.pos_x = self.maxspeed
        if self.pos_x <= -self.maxspeed:
            self.pos_x = -self.maxspeed

        self.pos += self.pos_x

        # Gravity
        if not self.collide(objects) and self.is_jumping == False:
            self.y += 200 * self.velocity_y * mandaw.dt
            self.velocity_y += 5 * mandaw.dt

        if self.collide(objects):
            self.velocity_y = 1
            self.maxspeed = 3

            if self.direction == 0 and not mandaw.controls.is_key_pressed(mandaw.keys["A"]):
                self.pos_x += 10 * mandaw.dt

                if self.pos_x >= 0:
                    self.pos_x = 0
            
            if self.direction == 1 and not mandaw.controls.is_key_pressed(mandaw.keys["D"]):
                self.pos_x -= 10 * mandaw.dt

                if self.pos_x <= 0:
                    self.pos_x = 0

        if not self.collide(objects):
            if self.direction == 0 and not mandaw.controls.is_key_pressed(mandaw.keys["A"]):
                self.pos_x += 0.1

                if self.pos_x >= 0:
                    self.pos_x = 0
            
            if self.direction == 1 and not mandaw.controls.is_key_pressed(mandaw.keys["D"]):
                self.pos_x -= 0.1

                if self.pos_x <= 0:
                    self.pos_x = 0
            
        # Platform collisions
        if self.collide(platform7):
            self.jump_y = 20
        if self.collide(platform10):
            self.jump_y = 20
        if self.collide(platform12):
            self.maxspeed = 5
        if self.collide(platform13):
            self.maxspeed = 5
        if self.collide(platform14):
            self.maxspeed = 5

        # Set the x position as the x variable
        self.x = self.pos

    def jump(self):
        # Jumping
        if self.is_jumping == False and mandaw.controls.is_key_pressed(mandaw.keys["SPACE"]):
            self.is_jumping = True
            if not self.collide(objects):
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
            window = mandaw,
            shape = "rect",
            width = 50,
            height = 10,
            x = x,
            y = y,
            color = "green"
        )

class JumpPlatform(GameObject):
    def __init__(self, x, y):
        super().__init__(
            window = mandaw,
            shape = "rect",
            width = 50,
            height = 10,
            x = x,
            y = y,
            color = "orange"
        )

class SpeedPlatform(GameObject):
    def __init__(self, x, y):
        super().__init__(
            window = mandaw,
            shape = "rect",
            width = 100,
            height = 10,
            x = x,
            y = y,
            color = "blue"
        )

class FinishBlock(GameObject):
    def __init__(self, x, y):
        super().__init__(
            mandaw,
            shape = "rect",
            width = 50,
            height = 10,
            x = x,
            y = y,
            color = "yellow"
        )

# Call the player
player = PlatformerController()

center_x = mandaw.width / 2
center_y = mandaw.height / 2

# Platforms
platform = Platform(center_x - 200, center_y + 170)
platform1 = Platform(center_x - 280, center_y + 140)
platform2 = Platform(center_x - 360, center_y + 110)
platform3 = Platform(center_x - 280, center_y + 80)
platform4 = Platform(center_x - 200, center_y + 50)
platform5 = Platform(center_x - 120, center_y + 20)

platform6 = Platform(center_x - 40, center_y - 10)
platform7 = JumpPlatform(center_x + 40, center_y + 100)
platform8 = Platform(center_x + 120, center_y - 40)
platform9 = Platform(center_x + 220, center_y - 40)
platform10 = JumpPlatform(center_x + 320, center_y - 40)

platform11 = Platform(center_x + 220, center_y - 220)
platform12 = SpeedPlatform(center_x + 80, center_y - 220)
platform13 = SpeedPlatform(center_x + -120, center_y - 220)
platform14 = SpeedPlatform(center_x + -320, center_y - 220)

finishBlock = FinishBlock(center_x + -400, center_y - 220)

# Add platforms to the object list
objects.append(ground)
objects.append(platform)
objects.append(platform1)
objects.append(platform2)
objects.append(platform3)
objects.append(platform4)
objects.append(platform5)
objects.append(platform6)
objects.append(platform7)
objects.append(platform8)
objects.append(platform9)
objects.append(platform10)
objects.append(platform11)
objects.append(platform12)
objects.append(platform13)
objects.append(platform14)
objects.append(finishBlock)

# Main Game Loop
while True:
    # Call the player functions
    player.movement()
    player.jump()

    # Draw the ground and player
    player.draw()
    ground.draw()
    platform.draw()
    platform1.draw()
    platform2.draw()
    platform3.draw()
    platform4.draw()
    platform5.draw()
    platform6.draw()
    platform7.draw()
    platform8.draw()
    platform9.draw()
    platform10.draw()
    platform11.draw()
    platform12.draw()
    platform13.draw()
    platform14.draw()

    finishBlock.draw()

    # Run the program
    mandaw.run()
