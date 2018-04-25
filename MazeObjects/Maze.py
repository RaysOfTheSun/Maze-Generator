from MazeObjects.Cell import Cell
from MazeObjects.Colors import Color
import pygame


class Maze:
    def __init__(self):
        surface_height, surface_width = 400, 400  # The dimensions of our py game window (height, width)
        self.cell_width = surface_width // 10  # The width and height of our square shaped cell
        self.rows, self.columns = surface_width // self.cell_width, surface_height // self.cell_width
        self.grid = []
        self.current = None
        self.__palette = Color()

        pygame.init()
        self.surface = pygame.display.set_mode((surface_height, surface_width))

    def create(self):
        """
        Creates the initial grid of cells
        :return:
        """
        for row in list(range(self.columns)):
            for column in list(range(self.columns)):
                grid_cell = Cell(row, column, self.cell_width)
                self.grid.append(grid_cell)

        self.grid[0].visited = True
        self.current = self.grid[0]

    def build(self):
        """
        Carves out the maze using Depth First Search and Recursive Backtracking
        :return:
        """
        clock = pygame.time.Clock()

        while True:
            user_action = pygame.event.poll()
            if user_action.type == pygame.QUIT:
                pygame.quit()
                break

            if self.grid:  # if there a cells in the grid, display them
                for grid_cell in self.grid:
                    grid_cell.draw(self.surface)

            pygame.display.flip()  # update the canvas so the grid will be shown after it is drawn

            clock.tick(5)

            self.current.highlight(self.surface, self.__palette.green, 255)

            chosen_index = self.current.get_neighbor(self.grid)
            if chosen_index is not None:
                self.grid[chosen_index].visited = True
                self.current = self.grid[chosen_index]
