import pygame

class Sprite:
    def __init__(self, window, image, x, y, size = (200, 200)):
        self.animations = {}
        self.image = pygame.image.load(image)
        if size is not None:
            self.image = pygame.transform.scale(self.image, size)
        self.window = window

        self.x = x
        self.y = y
        self.size = size

    def draw(self):
        self.window.window.blit(self.image, (self.x, self.y))

    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()

    def center(self):
        self.x = self.window.width / 2 - self.size[0]
        self.y = self.window.height / 2 - self.size[1]

    def resize(self, size):
        self.image = pygame.transform.scale(self.image, size)

    def add_animation(self, animation, name):
        self.animations[name] = {"frames": animation.frames, "length": animation.count, "cooldown": animation.anim_time,
                                 "count": 0, "folder": animation.folder}

    def play_animation(self, name, mirror=None):
        for i in self.animations:
            if i != name:
                self.animations[i]["count"] = 0
            else:
                self.animations[i]["count"] += self.animations[i]["cooldown"]
                if self.animations[i]["count"] >= self.animations[i]["length"]:
                    self.animations[i]["count"] = 0

                if self.size is None:
                    if mirror is None:
                        self.image = pygame.image.load(self.animations[i]["folder"] + "/" +
                                                       self.animations[i]["frames"][int(self.animations[i]["count"])])
                    elif mirror == "x":
                        self.image = pygame.transform.flip(pygame.image.load(self.animations[i]["folder"] + "/" +
                                                                             self.animations[i]["frames"][
                                                                                 int(self.animations[i]["count"])]),
                                                           True, False)
                    elif mirror == "y":
                        self.image = pygame.transform.flip(pygame.image.load(self.animations[i]["folder"] + "/" +
                                                                             self.animations[i]["frames"][
                                                                                 int(self.animations[i]["count"])]),
                                                           True, False)
                else:
                    if mirror is None:
                        self.image = pygame.transform.scale(pygame.image.load(self.animations[i]["folder"] + "/" +
                                                                              self.animations[i]["frames"][
                                                                                  int(self.animations[i]["count"])]),
                                                            self.size)
                    elif mirror == "x":
                        self.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load(self.animations[i]["folder"] + "/" +
                                                                     self.animations[i]["frames"][
                                                                         int(self.animations[i]["count"])]),
                                                   self.size), True, False)
                    elif mirror == "y":
                        self.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load(self.animations[i]["folder"] + "/" +
                                                                     self.animations[i]["frames"][
                                                                         int(self.animations[i]["count"])]),
                                                   self.size),
                            True, False)

                self.draw()
