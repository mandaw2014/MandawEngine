import pygame

class Line:
    def __init__(self, window, color, start_pos, end_pos):   
        self.window = window
        self.color = color
        self.start_pos = start_pos
        self.end_pos = end_pos

        pygame.draw.aaline(self.window.window, self.color, self.start_pos, self.end_pos)
