"""
MIT License

Copyright (c) 2021 Emc2356

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from typing import List, Iterable, Union
from typing import Tuple

import pygame
import random

import mandaw


class Particle:
    """
    Creates a particle

    Parameters:
    -----------
    WIN: pygame.surface.Surface
        the screen that the button is going to be drawn in
    x: int
        the x position of the particle
    y: int
        the y position of the particle
    vel_x: float
        the velocity of the particle in the x-axis
    vel_y: float
        the velocity of the particle in the y-axis
    shrink_amount: float
        how much will the particle be called per time
    size: float
        how big a particle is
    color: Tuple[int, int, int]
        the color of the particle
    collision_tolerance: float
        how close it has to be in a rect to trigger a collision
    gravity: float
        what gravity is going to be applied on the particle

    Methods:
    -----------
    draw():
        it draws the particle
    shrink(DeltaTime=1):
        it shrinks the particle
    activate_gravity(DeltaTime=1):
        it makes the particle be effected by gravity
    move(DeltaTime=1):
        it moves the particle
    update_rect():
        it updates the Rect of the particle
    randomize_vel():
        it randomizes the velocities (don't know why i even made it tbh)
    collide_with_rects(pygame_rects, DeltaTime=1):
        it does collisions with pygame rects
    """

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

    def __str__(self):
        return f"{self.size}"


class ParticleManager():
    """
    Creates a storage for the particles with more functions
    Parameters:
    -----------
    WIN: pygame.surface.Surface
        the screen that particles are going to be drawn in
    Methods:
    -----------
    draw():
        it draws the particles on the screen
    shrink():
        it shrinks the particles
    delete_particles():
        it deletes particles that have a size smaller than 0
    collide_rects(pygame_rects, DeltaTime):
        it checks for collisions with pygame rects
    update_rects():
        it updates the rects
    randomize_vels():
        it it randomizes the velocities of the particles (why did i even made this smh)
    move(DeltaTime=1):
        it moves the particle
    activate_gravity(DeltaTime=1):
        it applies the gravity to the particles
    get_particles():
        it returns a list of the particles
    add_particle(x, y, vel_x, vel_y, shrink_amount, size, color, collision_tolerance, gravity):
        it adds a new particle
    """

    def __init__(self, WIN: pygame.surface.Surface):
        self.__items: List[Particle] = []

    def draw(self) -> None:
        [text.draw() for text in self.__items]

    def shrink(self, dt: float = 1) -> None:
        [text.shrink(dt) for text in self.__items]

    def delete_particles(self) -> None:
        new_particles = [particle for particle in self.__items if particle.size > 0]
        self.__items = new_particles

    def collide_rects(self, rects: List[pygame.Rect], dt: float = 1) -> None:
        [particle.collide_with_rects(rects, dt) for particle in self.__items]

    def update_rects(self) -> None:
        [particle.update_rect() for particle in self.__items]

    def randomize_vels(self, limit_x: Tuple[float, float], limit_y: Tuple[float, float]) -> None:
        [particle.randomize_vel(limit_x, limit_y) for particle in self.__items]

    def move(self, dt: float = 1) -> None:
        [particle.move(dt) for particle in self.__items]

    def activate_gravity(self, dt: float = 1) -> None:
        [particle.activate_gravity(dt) for particle in self.__items]

    def get_particles(self) -> List[Particle]:
        return self.__items

    def add_particle(self,
                     x: int,
                     y: int,
                     vel_x: float,
                     vel_y: float,
                     shrink_amount: float,
                     size: float = 7,
                     color: Tuple[int, int, int] = (255, 255, 255),
                     collision_tolerance: float = 10,
                     gravity: float = 0.1) -> None:
        self.__items.append(
            Particle(self.WIN, x, y, vel_x, vel_y, shrink_amount, size, color, collision_tolerance, gravity))

    def __getitem__(self, item) -> Particle:
        return self.__items[item]

    def __iter__(self) -> Iterable[Particle]:
        return iter(self.__items)

    def __next__(self) -> Particle:
        try:
            item = self.__items[self.__i]
            self.__i += 1
        except IndexError:
            self.__i = 0
            item = self.__next__()

        return item

    def __reversed__(self) -> List[Particle]:
        reversed(self.__items)
        return self.__items


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
