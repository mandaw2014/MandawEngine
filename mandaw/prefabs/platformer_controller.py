from mandaw import *

class PlatformerController2D(GameObject):
    def __init__(self, window, x = 0, y = 0, centered = True):
        super().__init__(
            window,
            shape = "rect",
            width = 15,
            height = 30,
            x = x,
            y = y,
            color = "orange"
        )

        if centered == True:
            self.center()
        else:
            pass

         # Player's X Position
        self.pos_x = 0

        # Set the position as a variable
        self.pos = self.window.width / 2 - self.width

        self.is_jumping = False
        self.jump_y = 10

        self.direction = None

        self.velocity_y = 1

        # Player's speed and maxspeed
        self.speed = 15
        self.maxspeed = 3

        self.collision_objects = []
        self.ignore_speed = []

        self.window = window

    def movement(self, dt):
        # Player movement
        if self.window.input.get_key_pressed(self.window.input.keys["A"]):
            self.pos_x -= self.speed * dt
            self.direction = 0

        if self.window.input.get_key_pressed(self.window.input.keys["D"]):
            self.pos_x += self.speed * dt
            self.direction = 1

        # Momentum
        if self.pos_x >= self.maxspeed:
            self.pos_x = self.maxspeed
        if self.pos_x <= -self.maxspeed:
            self.pos_x = -self.maxspeed

        self.pos += self.pos_x

        # Gravity
        if not self.collide(self.collision_objects) and self.is_jumping == False:
            self.y += 3 * self.velocity_y
            self.velocity_y += 0.1

        if self.collide(self.collision_objects):
            self.velocity_y = 1

            if not self.collide(self.ignore_speed):
                self.maxspeed = 3

            if self.direction == 0 and not self.window.input.get_key_pressed(self.window.input.keys["A"]):
                self.pos_x += 10 * dt

                if self.pos_x >= 0:
                    self.pos_x = 0
            
            if self.direction == 1 and not self.window.input.get_key_pressed(self.window.input.keys["D"]):
                self.pos_x -= 10 * dt

                if self.pos_x <= 0:
                    self.pos_x = 0

        if not self.collide(self.collision_objects):
            if self.direction == 0 and not self.window.input.get_key_pressed(self.window.input.keys["A"]):
                self.pos_x += 0.1

                if self.pos_x >= 0:
                    self.pos_x = 0
            
            if self.direction == 1 and not self.window.input.get_key_pressed(self.window.input.keys["D"]):
                self.pos_x -= 0.1

                if self.pos_x <= 0:
                    self.pos_x = 0

        # Set the x position as the x variable
        self.x = self.pos

        self.jump()

    def jump(self):
        # Jumping
        if self.is_jumping == False and self.window.input.get_key_pressed(self.window.input.keys["SPACE"]):
            self.is_jumping = True
            if not self.collide(self.collision_objects):
                self.is_jumping = False

        if self.is_jumping == True:
            self.y -= self.jump_y
            self.jump_y -= 1

            if self.jump_y < -5:
                self.is_jumping = False
                self.jump_y = 10

if __name__ == "__main__":
    mandaw = Mandaw("PlatformerController2D", bg_color = "cyan")

    player = PlatformerController2D(mandaw, x = 0, y = 0, centered = True)

    ground = GameObject(mandaw, "rect", width = 5000, height = 100, x = 0, y = 500, color = "gray")
    ground.center_x()

    player.collision_objects.append(ground)

    @mandaw.draw
    def draw():
        player.draw()
        ground.draw()

    @mandaw.update
    def update(dt):
        player.movement(dt)
    
    mandaw.loop()