from MazeObjects.Cell import Cell
import pygame; import random


class Maze:
    def __init__(self):
        surface_height, surface_width = 400, 400  # The dimensions of our py game window (height, width)
        self.cell_width = surface_width // 10  # The width and height of our square shaped cell
        self.rows, self.columns = surface_width // self.cell_width, surface_height // self.cell_width
        self.grid = []
        self.current = None

        pygame.init()
        self.surface = pygame.display.set_mode((surface_height, surface_width))

    def create(self):
        for row in range(self.rows):
            for column in range(self.columns):
                grid_cell = Cell(row, column, self.cell_width)
                self.grid.append(grid_cell)

        self.current = self.grid[0]
        self.current.visited = True

    def build(self):
        while True:
            user_action = pygame.event.poll()
            if user_action.type == pygame.QUIT:
                pygame.quit()
                break

            if self.grid:  # if there a cells in the grid, display them
                for grid_cell in self.grid:
                    grid_cell.draw(self.surface)

                pygame.display.flip()  # update the canvas so the grid will be shown after it is drawn

