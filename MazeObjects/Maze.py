from MazeObjects.Cell import Cell
from MazeObjects.Colors import Color
import pygame
import random


class Maze:
    def __init__(self):
        """
        Initializes an instance of the Maze class
        """
        surface_height, surface_width = 600, 600   # The dimensions of our py game window (height, width)
        self.cell_width = surface_width // 10  # The width and height of our square shaped cell
        self.rows, self.columns = surface_height // self.cell_width, surface_width // self.cell_width
        self.grid_unvisited = []
        self.grid_visited = []  # This one will act as our stack
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
                grid_cell = Cell(column, row, self.cell_width)
                self.grid_unvisited.append(grid_cell)

        random_cell = random.choice(self.grid_unvisited)  # Start building from a random cell lol. Is that a good idea?
        self.grid_unvisited[self.grid_unvisited.index(random_cell)].visited = True
        self.current = self.grid_unvisited[self.grid_unvisited.index(random_cell)]

    def remove_walls(self, current, neighbor):
        """
        Removes the walls between the two given cells
        :param current: The current cell
        :param neighbor: The neighbor of the current cell
        :return: None
        """
        current_idx = self.grid_unvisited.index(current)
        neighbor_idx = self.grid_unvisited.index(neighbor)

        if neighbor.x_coordinate - current.x_coordinate == -1:
            current.walls[2]['left'].show = False
            neighbor.walls[3]['right'].show = False
        elif neighbor.x_coordinate - current.x_coordinate == 1:
            current.walls[3]['right'].show = False
            neighbor.walls[2]['left'].show = False
        elif current.y_coordinate - neighbor.y_coordinate == 1:
            current.walls[0]['top'].show = False
            neighbor.walls[1]['bottom'].show = False
        elif current.y_coordinate - neighbor.y_coordinate == -1:
            current.walls[1]['bottom'].show = False
            neighbor.walls[0]['top'].show = False

        self.current = current
        self.grid_unvisited[current_idx] = current
        self.grid_unvisited[neighbor_idx] = neighbor

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

            if self.grid_unvisited:  # if there a cells in the grid, display them
                for grid_cell in self.grid_unvisited:
                    grid_cell.draw(self.surface)

            pygame.display.flip()  # update the canvas so the grid will be shown after it is drawn

            clock.tick(60)  # Slows down the frame rate. I need to see if what it's doing is right

            self.current.highlight(self.surface, self.__palette.green, 255)

            chosen_index = self.current.get_neighbor(self.grid_unvisited)  # Step 2.1
            if chosen_index is not None:
                self.grid_visited.append(self.current)  # Step 2.2
                self.grid_unvisited[chosen_index].visited = True
                self.remove_walls(self.current, self.grid_unvisited[chosen_index])
                self.current = self.grid_unvisited[chosen_index]
            elif self.grid_visited:
                self.current = self.grid_visited.pop()
