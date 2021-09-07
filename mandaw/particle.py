from typing import List, Union
from typing import Tuple

import pygame
import random

import mandaw


class Particle:

    def __init__(self, WIN: pygame.surface.Surface, x: int, y: int, vel_x: float, vel_y: float, shrink_amount: float,
                 size: float = 7, color: Tuple[int, int, int] = (255, 255, 255), collision_tolerance: float = 10,
                 gravity: float = 0.1):
        self.WIN: pygame.surface.Surface = WIN
        self.x: int = x
        self.y: int = y
        self.vel_x: float = vel_x
        self.vel_y: float = vel_y
        self.shrink_amount: float = shrink_amount
        self.size: float = size
        self.color: Tuple[int, int, int] = color
        self.collision_tolerance: float = collision_tolerance
        self.gravity: float = gravity
        self.rect: pygame.Rect = None
        self.update_rect()

    def draw(self) -> None:
        pygame.draw.circle(self.WIN, self.color, (self.x, self.y), self.size)

    def shrink(self, dt: float = 1) -> None:
        self.size -= self.shrink_amount * dt
        self.update_rect()

    def activate_gravity(self, dt: float):
        self.vel_y += self.gravity * dt
        self.update_rect()

    def move(self, dt: float):
        self.x += self.vel_x * dt
        self.y += self.vel_y * dt

    def update_rect(self):
        self.rect: pygame.Rect = pygame.Rect(self.x - self.size / 2, self.y - self.size / 2, self.size, self.size)

    def randomize_vel(self, limit_x: Tuple[float, float], limit_y: Tuple[float, float]) -> None:
        self.vel_x = random.uniform(*limit_x)
        self.vel_y = random.uniform(*limit_y)

    def collide_with_rects(self, rects: List[pygame.Rect], dt: float = 1) -> None:
        for rect in rects:
            rect = rect.copy()
            rect.x -= self.collision_tolerance
            rect.y -= self.collision_tolerance
            rect.w += self.collision_tolerance * 2
            rect.h += self.collision_tolerance * 2
            if rect.colliderect(self.rect):
                if abs(rect.top - self.rect.bottom) < self.collision_tolerance and self.vel_y > 0:
                    self.vel_y *= (-0.75) * dt
                    self.y += (self.vel_y * 2) * dt
                    self.update_rect()
                if abs(rect.bottom - self.rect.top) < self.collision_tolerance and self.vel_y < 0:
                    self.vel_y *= (-0.75) * dt
                    self.y += (self.vel_y * 2) * dt
                    self.update_rect()
                if abs(rect.right - self.rect.left) < self.collision_tolerance and self.vel_x < 0:
                    self.vel_x *= (-0.75) * dt
                    self.x += (self.vel_x * 2) * dt
                    self.update_rect()
                if abs(rect.left - self.rect.right) < self.collision_tolerance and self.vel_x > 0:
                    self.vel_x *= (-0.75) * dt
                    self.x += (self.vel_x * 2) * dt
                    self.update_rect()



class ParticleSpawner:
    def __init__(self, window: mandaw.Mandaw, part_count: Union[int, list, tuple] = 1,
                 pos: Union[list, tuple] = (0, 0), size: Union[list, tuple, int] = 20,
                 velocityx: Union[float, list, tuple] = 1, velocityy: Union[float, list, tuple] = 1,
                 shrink: Union[float, int, list, tuple] = 0.1, color: Union[str, mandaw.Color, tuple, list] = "white",
                 collide: bool = False, gravity=0, collide_rects=None):
        if collide_rects is None:
            collide_rects = []
        self.window = window
        self.part_count = part_count
        self.pos = pos
        self.size = size
        self.shrink = shrink
        self.color = color
        self.collide = collide
        self.particles = []
        self.velocityx = velocityx
        self.velocityy = velocityy
        self.collide_rects = collide_rects
        self.gravity = gravity
        if type(part_count) != int:
            part_count = random.randint(*part_count)

        for i in range(part_count):
            if type(size) != int:
                self.size = random.randint(*size)
            if type(velocityx) != int:
                self.velocityx = random.uniform(*velocityx)
            if type(velocityy) != int:
                self.velocityy = random.uniform(*velocityy)
            self.particles.append(Particle(self.window.window, self.pos[0], self.pos[1], self.velocityx, self.velocityy,
                                           self.shrink,
                                           self.size, gravity=self.gravity, collision_tolerance=10, color=self.color))

    def draw(self):
        if len(self.particles) > 0:
            for i in self.particles:
                i.draw()
                i.move(self.window.dt)
                i.activate_gravity(self.window.dt)
                i.shrink(self.window.dt)
                if self.collide:
                    i.collide_with_rects(self.collide_rects, self.window.dt)
                if i.size < 0:
                    self.particles.remove(i)
