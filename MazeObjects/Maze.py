from MazeObjects.Cell import Cell
import pygame


class Maze:
    def __init__(self):
        surface_height, surface_width = 400, 400  # The dimensions of our py game window (height, width)
        self.cell_width = surface_width // 10  # The width of our square shaped cell
        self.rows, self.columns = surface_width // self.cell_width, surface_height // self.cell_width
        self.grid = []

        pygame.init()
        self.surface = pygame.display.set_mode((surface_height, surface_width))

    def __create(self):
        for row in range(self.rows):
            for column in range(self.columns):
                grid_cell = Cell(row, column, self.cell_width)
                self.grid.append(grid_cell)
                grid_cell.draw(self.surface)

    def build(self):
        self.__create()
        while True:
            user_action = pygame.event.poll()
            if user_action.type == pygame.QUIT:
                pygame.quit()
                break

            for grid_cell in self.grid:
                grid_cell.draw(self.surface)

            print("cell object count: {}".format(len(self.grid)))
            pygame.display.flip()  # update the canvas so the grid will be shown after it is drawn

    

