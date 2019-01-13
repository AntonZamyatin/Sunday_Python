"""Game classes."""
import numpy as np
import pygame
import random
from params import *
from math import sqrt, tan, pi


class Particle(object):
    """Particles."""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 6
        self.finished = False
        self.color = white

    def intersect(self, array):
        def distance(x1, y1, x2, y2):
            return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        result = False
        d = 10
        for part in array:
            if distance(part.x, part.y, self.x, self.y) < d:
                result = True
        return result

    def update(self):
        prev_y = self.y
        self.x -= 1
        self.y += random.randint(-3, 3)
        while self.y > 150 + self.x * tan(pi / 6):
            self.y -= 1
        while self.y < 150 - self.x * tan(pi / 6):
            self.y += 1
        self.color = (100 + random.randint(-50, 50),
                      255 + random.randint(-50, 0),
                      255)
        if self.x < random.randint(1, 10):
            self.finished = True
            print(self.x, self.y)


    def draw(self, screen, color):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
        pygame.draw.circle(screen, self.color, (self.x, 300 - self.y), self.r)
