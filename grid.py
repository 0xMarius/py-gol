import pygame
import random


# cell size = 25 x 25 pixels
# cells = 750 / 25 = 30
class Grid:
    def __init__(self, width, height, cell_size):

        # floored attributes
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.cell_size = cell_size
        self.cells = [[0 for _ in range(self.columns)] for _ in range(self.rows)]

    def draw(self, window):
        for row in range(self.rows):
            for column in range(self.columns):
                # assign green color if cell is alive
                color = (0, 255, 0) if self.cells[row][column] else (55, 55, 55)
                # 1 - surface; 3 - x, y, width, height
                # to create grid lines, we subtract 1 from cell_size
                pygame.draw.rect(
                    window,
                    color,
                    (
                        column * self.cell_size,
                        row * self.cell_size,
                        self.cell_size - 1,
                        self.cell_size - 1,
                    ),
                )

    def fill_random(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = random.choice([0, 0, 0, 1])

    def clear(self):
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = 0

    def toggle_cell(self, row, column):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.cells[row][column] = not self.cells[row][column]
