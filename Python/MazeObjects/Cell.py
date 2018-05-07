import pygame
from MazeObjects.Colors import Color
from MazeObjects.Wall import Wall
import random


class Cell:
    def __init__(self, x_coordinate, y_coordinate, width):
        """
        Creates an instance of the cell class
        :param x_coordinate:
        :param y_coordinate:
        :param width: How wide and tall the cell would be.
        """
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.__width = width
        self.visited = False
        self.walls = self.build_walls()
        self.__palette = Color()

    def build_walls(self):
        """
        Defines each wall of the cell
        :return: a collection of walls for the cell
        """
        x = self.x_coordinate * self.__width
        y = self.y_coordinate * self.__width

        top = Wall((x, y), ((x + self.__width), y))
        bottom = Wall((x, y + self.__width), ((x + self.__width), y + self.__width))
        left = Wall((x, y), (x, (y + self.__width)))
        right = Wall(((x + self.__width), y), ((x + self.__width), (y + self.__width)))

        walls = {'top': top, 'bottom': bottom, 'left': left, 'right': right}

        return walls

    def draw(self, surface):
        """
        draws a square shaped cell on the canvas/screen/whatever
        Each cell is composed of four sides. Each side is an individual line.
        :return: nothing
        """

        for wall in self.walls:
            if self.walls[wall].show:
                self.walls[wall].draw(surface)

        if self.visited:
            self.highlight(surface, self.__palette.purple, 50)

    def highlight(self, surface, color, alpha):
        """
        Fills the space occupied by the cell with the specified color
        :param surface: The canvas where the cell is drawn
        :param color: The color to be used to fill the cell
        :param alpha: The alpha level to be used along with the specified color
        :return: None
        """
        x = self.x_coordinate * self.__width
        y = self.y_coordinate * self.__width
        rectangle = pygame.Surface((self.__width, self.__width))
        rectangle.fill(color)
        rectangle.set_alpha(alpha)
        surface.blit(rectangle, (x, y))

    @staticmethod
    def get_cell(x_coordinate: int, y_coordinate: int, column_count: int=10)->int:
        """
        Gets the index of a cell from the given set of coordinates
        :param (int) x_coordinate: the x coordinate of the base cell
        :param (int) y_coordinate: the y coordinate of the base cell
        :param (int) column_count: the number of columns that the grid has
        :return: (int) the index of the specific cell in the grid
        """
        if (x_coordinate < 0) or (y_coordinate < 0) or (x_coordinate > column_count - 1) \
                or (y_coordinate > column_count - 1):
            return -1

        # print("index: {} ".format(x_coordinate + y_coordinate * column_count))
        return x_coordinate + (y_coordinate * column_count)

    def get_neighbor(self, cells, width):
        indexes = [self.get_cell(self.x_coordinate, self.y_coordinate - 1, width),  # top side
                   self.get_cell(self.x_coordinate, self.y_coordinate + 1, width),  # bottom side
                   self.get_cell(self.x_coordinate - 1, self.y_coordinate, width),  # left side
                   self.get_cell(self.x_coordinate + 1, self.y_coordinate, width)]  # right side

        neighbors = []

        for index in indexes:
            if index != -1 and cells[index].visited is False:
                neighbors.append(cells[index])

        if neighbors:
            v = random.choice(neighbors)
            return cells.index(v)
