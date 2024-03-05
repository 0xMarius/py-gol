# The Rules
# Underpopulation: A live cell with fewer than two lviing neighbors dies

# Stasis: A live cell with two or three live neighbors lives on to the next generation

# Overpopulation: A live cell with more than three live neighbors dies

# Reproduction: A dead cell with exactly three live neighbros becomes a live cell

# The Rules: reduced
# Rule 1.: If a cell is alive, it dies when it has fewer than 2 or more than 3 live neighbors, else it stays alive

# Rule 2.: If a cell is dead, it can come alive only if it has exactly 3 live neighbors, else it stays dead

from grid import Grid


class Simulation:
    def __init__(self, width, height, cell_size):
        self.grid = Grid(width, height, cell_size)
        self.temp_grid = Grid(width, height, cell_size)

        self.rows = height // cell_size
        self.columns = width // cell_size

        self.run = False

    def draw(self, window):
        self.grid.draw(window)

    def count_live_neighbors(self, grid, row, column):
        # cell has 8 neighbors - 2 hor, 2 vert, 4 diag
        live_neighbors = 0
        neighbor_offsets = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        for offset in neighbor_offsets:
            # To correctly count the live neighbors, we will establish a Toroidal grid, a grid whose edges wrap around
            new_row = (row + offset[0]) % self.rows
            new_column = (column + offset[1]) % self.columns

            if self.grid.cells[new_row][new_column] == 1:
                live_neighbors += 1

        return live_neighbors

    def update(self):
        if self.is_running():
            # Naive approach
            for row in range(self.rows):
                for column in range(self.columns):
                    live_neighbors = self.count_live_neighbors(self.grid, row, column)
                    cell_value = self.grid.cells[row][column]

                    if cell_value == 1:
                        if live_neighbors > 3 or live_neighbors < 2:
                            self.temp_grid.cells[row][column] = 0
                        else:
                            self.temp_grid.cells[row][column] = 1
                    else:
                        if live_neighbors == 3:
                            self.temp_grid.cells[row][column] = 1
                        else:
                            self.temp_grid.cells[row][column] = 0

            for row in range(self.rows):
                for column in range(self.columns):
                    self.grid.cells[row][column] = self.temp_grid.cells[row][column]

    def is_running(self):
        return self.run

    def start(self):
        self.run = True

    def stop(self):
        self.run = False

    def clear(self):
        self.grid.clear()

    def create_random_state(self):
        self.grid.fill_random()

    def toggle_cell(self, row, column):
        self.grid.toggle_cell(row, column)
