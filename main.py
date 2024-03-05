import pygame
import sys
from sim import Simulation

pygame.init()

GREY = (29, 29, 29)
WINDOW_WIDTH = 750
WINDOW_HEIGHT = 750
CELL_SIZE = 25
FPS = 30

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game of Life")

clock = pygame.time.Clock()
simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

while True:
    # 1. Event handling
    # 1.1. Gets all the events that pygame recognizes, puts them in a list
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row = pos[1] // CELL_SIZE
            column = pos[0] // CELL_SIZE
            simulation.toggle_cell(row, column)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                simulation.start()
                pygame.display.set_caption("Game of Life is running")
            elif event.key == pygame.K_s:
                simulation.stop()
                pygame.display.set_caption("Game of Life is paused")
            elif event.key == pygame.K_c:
                simulation.clear()
            elif event.key == pygame.K_r:
                simulation.create_random_state()

    # 2. Updating state
    simulation.update()

    # 3. Drawing objects
    window.fill(GREY)
    simulation.draw(window)

    pygame.display.update()
    clock.tick(FPS)
