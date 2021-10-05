from mandaw import *

class Player(Sprite):
    def __init__(self, window):
        super().__init__(
            window,
            image = "./assets/StickMan.png",
            x = 0,
            y = 300,
            size = (80, 80)
        )

        self.center_x()

        self.window = window

        self.objects = []

        # Player's X Position
        self.pos_x = 0

        self.count = 0
        self.highscore_count = 0

        # Set the position as a variable
        self.pos = 800 / 2 - 100

        self.is_jumping = False
        self.jump_y = 10

        self.direction = None

        self.canjump = False

        self.velocity_y = 1

        self.enabled = True

        self.jump_sound = Audio("./assets/jump1.wav", 0.5)
        self.hit = Audio("./assets/hit1.wav", 0.5)

        # Player's speed and maxspeed
        self.speed = 15
        self.maxspeed = 3

        self.attack = Animation("./assets/attack", 0.3)

        self.add_animation(self.attack, "attack")

    def movement(self):
        # Player movement
        if self.window.input.get_key_pressed(self.window.keys["A"]):
            if self.enabled == True:
                self.pos_x -= self.speed * self.window.dt
                self.direction = 0
                self.play_animation("attack")

        if self.window.input.get_key_pressed(self.window.keys["D"]):
            if self.enabled == True:
                self.pos_x += self.speed * self.window.dt
                self.direction = 1
                self.play_animation("attack", "x")

        # Momentum
        if self.pos_x >= self.maxspeed:
            self.pos_x = self.maxspeed
        if self.pos_x <= -self.maxspeed:
            self.pos_x = -self.maxspeed

        self.pos += self.pos_x

        # Gravity
        if not self.collide(self.objects) and self.is_jumping == False:
            self.y += 3 * self.velocity_y
            self.velocity_y += 0.1

        if self.collide(self.objects):
            self.velocity_y = 1
            self.maxspeed = 4

            if self.direction == 0 and not self.window.input.get_key_pressed(self.window.keys["A"]):
                self.pos_x += 10 * self.window.dt

                if self.pos_x >= 0:
                    self.pos_x = 0
            
            if self.direction == 1 and not self.window.input.get_key_pressed(self.window.keys["D"]):
                self.pos_x -= 10 * self.window.dt

                if self.pos_x <= 0:
                    self.pos_x = 0

        if not self.collide(self.objects):
            if self.direction == 0 and not self.window.input.get_key_pressed(self.window.keys["A"]):
                self.pos_x += 0.1

                if self.pos_x >= 0:
                    self.pos_x = 0
            
            if self.direction == 1 and not self.window.input.get_key_pressed(self.window.keys["D"]):
                self.pos_x -= 0.1

                if self.pos_x <= 0:
                    self.pos_x = 0

        # Set the x position as the x variable
        self.x = self.pos

    def jump(self):
        # Jumping
        if self.collide(self.objects):
            self.canjump = True
        else:
            self.canjump = False

        if self.is_jumping == False and self.window.input.get_key_pressed(self.window.keys["SPACE"]):
            self.is_jumping = True

            if self.canjump == True:
                self.jump_sound.play()

            if not self.collide(self.objects):
                self.is_jumping = False

        if self.is_jumping == True:
            self.y -= self.jump_y
            self.jump_y -= 1

            if self.jump_y < -5:
                self.is_jumping = False
                self.jump_y = 10

    def dead(self):
        self.enabled = False
        self.pos_x = self.window.width / 2 - 40
        self.pos = self.window.width / 2 - 40
        self.velocity_y = 0