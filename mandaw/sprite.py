import pygame

class Sprite:
    def __init__(self, window, image, x, y, width = 200, height = 200):
        self.animations = {}
        self.image = pygame.image.load(image)

        if width and height is not None:
            self.image = pygame.transform.scale(self.image, (width, height))
        
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(0, 0, 0, 0)

    def draw(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.window.window.blit(self.image, (self.x, self.y))

    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()

    def center(self):
        self.x = self.window.width / 2 - self.width
        self.y = self.window.height / 2 - self.height

    def center_x(self):
        self.x = self.window.width / 2 - self.width

    def center_y(self):
        self.y = self.window.height / 2 - self.height

    def collide(self, rect):
        if type(rect) != list:
            return self.rect.colliderect(rect)
        elif type(rect) == list:
            return self.rect.collidelistall(rect)
        else:
            print("MandawError: sorry but when you typed collide(object), the object wasnt a string or a list. see "
                  "you soon :)")

    def resize(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))

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

                if self.width and self.height is None:
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
                                                            (self.width, self.height))
                    elif mirror == "x":
                        self.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load(self.animations[i]["folder"] + "/" +
                                                                     self.animations[i]["frames"][
                                                                         int(self.animations[i]["count"])]),
                                                   (self.width, self.height)), True, False)
                    elif mirror == "y":
                        self.image = pygame.transform.flip(
                            pygame.transform.scale(pygame.image.load(self.animations[i]["folder"] + "/" +
                                                                     self.animations[i]["frames"][
                                                                         int(self.animations[i]["count"])]),
                                                   (self.width, self.height)),
                            True, False)

                self.draw()
             
if __name__ == '__main__':
    from mandaw import *
    import os

    mandaw = Mandaw()

    path = os.path.dirname(os.path.abspath(__file__))
    bird = os.path.join(path, "./assets/bird.jpeg")

    image = Sprite(mandaw, bird, 0, 0)

    @mandaw.draw
    def draw():
        image.draw()
    
    mandaw.loop()