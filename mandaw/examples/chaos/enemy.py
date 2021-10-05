from mandaw import *
import random
import pygame

class Enemy(GameObject):
    def __init__(self, window, player, main_menu, x):
        super().__init__(
            window,
            shape = "rect",
            width = 15,
            height = 30,
            x = x,
            y = 400,
            color = "red" 
        )

        self.player = player
        self.window = window
        self.main_menu = main_menu

        self.hit = False

        self.speed = 3

    def movement(self):
        dirvect = pygame.math.Vector2(self.player.x - self.x, self.player.y - self.y)
        if dirvect != 0:
            dirvect.normalize()
        dirvect.scale_to_length(self.speed)

        if self.player.enabled == True:
            self.move_ip(dirvect)

        if not self.collide(self.player.objects):
            self.y += 100 * self.window.dt

        if self.hit == True:
            self.x = random.randint(90, 625)
            self.y = 460

            if self.collide(self.player):
                self.x = random.randint(90, 625)

            self.hit = False

        if self.collide(self.player):
            if not self.window.input.get_key_pressed(self.window.keys["A"]):
                if not self.window.input.get_key_pressed(self.window.keys["D"]):
                    if self.hit == False:
                        self.player.dead()
                        self.main_menu.enabled = True

            if self.player.direction == 0 and self.player.x < self.x:
                self.player.dead()
                self.main_menu.enabled = True
            if self.player.direction == 1 and self.player.x > self.x:
                self.player.dead()
                self.main_menu.enabled = True