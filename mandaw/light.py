from typing import Union

import pygame
from pygame.surface import Surface, SurfaceType

import mandaw


class Light:
    light_mask: Union[Surface, SurfaceType]
    light_filter: Surface

    def __init__(self, window: mandaw.Mandaw, mask_img):
        self.window = window
        self.mask = mask_img

    def light_init(self, pos):
        self.pos = pos
        self.light_mask = pygame.image.load(self.mask)
        self.light_filter = pygame.surface.Surface((self.window.width, self.window.height))
        self.light_filter.fill(pygame.color.Color("Gray"))
        self.light_filter.blit(self.light_mask, pos)
    def draw(self):
        self.window.window.blit(self.light_filter, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
        
if __name__ == '__main__':
    from mandaw import *

    mandaw = Mandaw(bg_color="red")
    light = Light(mandaw, "assets/circle.png")
    light.light_init((100, 100))

    while True:
        light.draw()
        mandaw.run()

