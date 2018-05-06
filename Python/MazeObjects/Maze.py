from MazeObjects.Cell import Cell
from MazeObjects.Colors import Color
from PathFinding.Pathfinder import Pathfinder
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
        self.grid = []
        self.grid_visited = []  # This one will act as our stack for cells that have been previously visited.
        self.current = None
        self.__palette = Color()
        self.pathfinder = None
        self.path_finding = False

        pygame.init()
        self.surface = pygame.display.set_mode((surface_height, surface_width))
        pygame.display.set_caption("Maze Generator")

    def create(self):
        """
        Creates the initial grid of cells
        :return: None
        """
        for row in list(range(self.columns)):
            for column in list(range(self.columns)):
                grid_cell = Cell(column, row, self.cell_width)
                self.grid.append(grid_cell)

        random_cell = random.choice(self.grid)  # Start building from a random cell lol. Is that a good idea?
        self.grid[self.grid.index(random_cell)].visited = True  # set that cell's properties first
        self.current = self.grid[self.grid.index(random_cell)]  # assign it as the current cell
        self.pathfinder = Pathfinder(self.grid, (9, 9))
        # self.grid[1 + 0].highlight(self.surface, self.__palette.white, 255)

    def remove_walls(self, current, neighbor):
        """
        Removes the walls between the two given cells
        :param current: The current cell
        :param neighbor: The neighbor of the current cell
        :return: None
        """
        current_idx = self.grid.index(current)
        neighbor_idx = self.grid.index(neighbor)

        if (neighbor.x_coordinate - current.x_coordinate) == -1:
            current.walls['left'].show = False
            neighbor.walls['right'].show = False
        elif (neighbor.x_coordinate - current.x_coordinate) == 1:
            current.walls['right'].show = False
            neighbor.walls['left'].show = False
        elif (current.y_coordinate - neighbor.y_coordinate) == 1:
            current.walls['top'].show = False
            neighbor.walls['bottom'].show = False
        elif (current.y_coordinate - neighbor.y_coordinate) == -1:
            current.walls['bottom'].show = False
            neighbor.walls['top'].show = False

        self.current = current
        self.grid[current_idx] = current
        self.grid[neighbor_idx] = neighbor

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

            clock.tick(60)  # Slows down the frame rate. I need to see if what it's doing is right
            # I also think the animation is fancy lol

            if not self.path_finding:
                self.current.highlight(self.surface, self.__palette.yellow, 255)  # Just so I know where I am in the grid
            else:
                self.current.highlight(self.surface, self.__palette.white, 255)  # Just so I know where I am in the grid

            chosen_index = self.current.get_neighbor(self.grid)  # Step 2.1
            if chosen_index is not None:
                self.grid_visited.append(self.current)  # Step 2.2
                self.grid[chosen_index].visited = True
                self.remove_walls(self.current, self.grid[chosen_index])
                self.current = self.grid[chosen_index]
            elif self.grid_visited:  # backtrack
                self.current = self.grid_visited.pop()
            else:
                clock.tick(20)  # Slows down the frame rate so the path finder can be properly seen as it searches
                if self.grid.index(self.current) != 99:
                    self.path_finding = True
                    # All the tiles in the grid has been visited and the maze has been carved out.
                    # This is where the pathfinder will come in
                    pathfinder = self.grid[self.pathfinder.x_coordinate + self.pathfinder.y_coordinate * self.columns]
                    self.current = pathfinder
                    self.pathfinder.path_find()

