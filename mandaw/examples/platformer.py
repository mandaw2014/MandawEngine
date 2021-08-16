from mandaw import *

# Window
mandaw = Mandaw("Platformer", bg_color = "cyan")

# Ground
ground = GameObject(mandaw.window, mandaw.width / 2 - 500, 500, "gray", 1000, 100)

# Player
class PlatformerController(GameObject):
    def __init__(self):
        super().__init__(
            mandaw.window,
            mandaw.width / 2 - 15,
            mandaw.height / 2 - 35,
            "orange",
            30,
            70
        )
        
        # Player Speed
        self.speed = 3
        # Set the position as a variable
        self.pos = mandaw.width / 2 - self.width

    def movement(self):
        # Player movement
        if mandaw.keys[mandaw.A]:
            self.pos -= 1 * self.speed
        if mandaw.keys[mandaw.D]:
            self.pos += 1 * self.speed

        # Gravity
        if not self.colliderect(ground):
            self.y += 3

        # Set the x position as the x variable
        self.x = self.pos

    def jump(self):
        # Jumping
        if self.colliderect(ground):
            self.y -= 100

# Call the player
player = PlatformerController()

# Main Game Loop
while True:
    # Call the player functions
    player.movement()

    if mandaw.keys[mandaw.SPACE]:
        player.jump()

    # Draw the ground and player
    ground.draw_rect()
    player.draw_rect()

    # Run the program
    mandaw.run()