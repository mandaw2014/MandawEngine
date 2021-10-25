from mandaw import *
from mandaw.prefabs.platformer_controller import PlatformerController2D

# Window
mandaw = Mandaw("Platformer!", bg_color = "cyan")

# Ground
ground = GameObject(mandaw, shape = "rect", width = 5000, height = 100, x = mandaw.width / 2 - 500, y = 500, color = "gray")

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
player = PlatformerController2D(mandaw, 0, 0, True)
player.y = 400

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
player.collision_objects.append(ground)
player.collision_objects.append(platform)
player.collision_objects.append(platform1)
player.collision_objects.append(platform2)
player.collision_objects.append(platform3)
player.collision_objects.append(platform4)
player.collision_objects.append(platform5)
player.collision_objects.append(platform6)
player.collision_objects.append(platform7)
player.collision_objects.append(platform8)
player.collision_objects.append(platform9)
player.collision_objects.append(platform10)
player.collision_objects.append(platform11)
player.collision_objects.append(platform12)
player.collision_objects.append(platform13)
player.collision_objects.append(platform14)
player.collision_objects.append(finishBlock)

@mandaw.draw
def draw():
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

# Main Game Loop
@mandaw.update
def update(dt):
    player.movement(dt)

    if player.collide(platform7):
        player.jump_y = 20
    if player.collide(platform10):
        player.jump_y = 20
    if player.collide(platform12):
        player.maxspeed = 5
    if player.collide(platform13):
        player.maxspeed = 5
    if player.collide(platform14):
        player.maxspeed = 5

# Run the program
mandaw.loop()
