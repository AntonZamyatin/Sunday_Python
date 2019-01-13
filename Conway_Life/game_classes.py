"""Game classes."""
import numpy as np
import pygame
from params import *


class Field(object):
    """Class for game field."""

    def __init__(self, screen, F_SIZE, CELL_WIDTH):
        """Field initialisation."""
        self.width = F_SIZE[0] // CELL_WIDTH
        self.higth = F_SIZE[1] // CELL_WIDTH
        self.size = self.width * CELL_WIDTH, self.higth * CELL_WIDTH
        self.cell_width = CELL_WIDTH
        self.screen = screen
        self.array = np.zeros((self.width, self.higth), dtype=int)
        self.tmp = np.zeros((self.width, self.higth), dtype=int)

    def draw_grid(self, color):
        """Grid drawing method."""
        x = 0
        y = 0
        while x <= self.size[0]:
            pygame.draw.line(self.screen, color, (x, 0), (x, self.size[1]))
            x += self.cell_width
        while y <= self.size[1]:
            pygame.draw.line(self.screen, color, (0, y), (self.size[0], y))
            y += self.cell_width

    def mouse_fill(self, x, y, val):
        """Method. Fills array by mouse coords."""
        self.array[x // self.cell_width, y // self.cell_width] = val

    def update(self):
        """Method. Updates field."""
        w = self.width
        h = self.higth
        self.tmp = np.copy(self.array)
        for x in range(self.width):
            for y in range(self.higth):
                neighbors = 0
                if self.array[(x - 1) % w, (y - 1) % h] == 33: neighbors += 1
                if self.array[(x) % w, (y - 1) % h] == 33: neighbors += 1
                if self.array[(x + 1) % w, (y - 1) % h] == 33: neighbors += 1
                if self.array[(x - 1) % w, (y) % h] == 33: neighbors += 1
                if self.array[(x + 1) % w, (y) % h] == 33: neighbors += 1
                if self.array[(x - 1) % w, (y + 1) % h] == 33: neighbors += 1
                if self.array[(x) % w, (y + 1) % h] == 33: neighbors += 1
                if self.array[(x + 1) % w, (y + 1) % h] == 33: neighbors += 1
                if self.array[x, y] == 33:
                    if neighbors < 2: self.tmp[x, y] = 32
                    if neighbors > 3: self.tmp[x, y] = 32
                else:
                    if neighbors == 3:
                        self.tmp[x, y] = 33
                    elif self.tmp[x, y] > 1:
                        self.tmp[x, y] -= 1

        self.array = self.tmp

    def clear(self):
        self.array = np.zeros((self.width, self.higth), dtype=int)

    def draw(self):
        """Method. Draws current field state."""
        self.screen.fill(black)
        #self.draw_grid(d_green)

        def new_rect(color, x, y):
            pygame.draw.rect(self.screen, color,
                             (x * self.cell_width + 1,
                              y * self.cell_width + 1,
                              self.cell_width - 1,
                              self.cell_width - 1))

        for x in range(self.width):
            for y in range(self.higth):
                if self.array[x, y] == 33:
                    new_rect(blue, x, y)
                elif self.array[x, y] > 30:
                    new_rect(green2, x, y)
                elif self.array[x, y] > 25:
                    new_rect(green3, x, y)
                elif self.array[x, y] > 1:
                    new_rect(green4, x, y)
                elif self.array[x, y] == 1:
                    new_rect(green5, x, y)
