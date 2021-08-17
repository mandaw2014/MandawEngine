import pygame

class Line:
    def __init__(self, window, color, width, height):   
        self.window = window
        self.color = color
        self.width = width
        self.height = height

        pygame.draw.aaline(self.window.window, self.color, self.width, self.height)