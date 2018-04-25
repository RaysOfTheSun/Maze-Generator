import pygame
from MazeObjects.Colors import Color
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
        self.walls = [True, True, True, True]
        self.__palette = Color()

    def draw(self, surface):
        """
        draws a square shaped cell on the canvas/screen/whatever
        Each cell is composed of four sides. Each side is an individual line.
        :return: nothing
        """
        x = self.x_coordinate * self.__width
        y = self.y_coordinate * self.__width

        """
        Some clean up plan:
        Create a list of wall objects per cell so we could easily modify its attributes
        if wall.show is false: show the wall.
        for wall in self.walls: if wall.show: wall.draw(surface)
        """

        # draw upper side of the cell
        if self.walls[0]:
            pygame.draw.line(surface, self.__palette.white, (x, y), ((x + self.__width), y))
        # draw the bottom side of the cell
        if self.walls[1]:
            pygame.draw.line(surface, self.__palette.white, (x, y + self.__width),
                             ((x + self.__width), y + self.__width))
        # draw the left side of the cell
        if self.walls[2]:
            pygame.draw.line(surface, self.__palette.white, (x, y), (x, (y + self.__width)))
        # draw the right side of the cell
        if self.walls[3]:
            pygame.draw.line(surface, self.__palette.white, ((x + self.__width), y),
                             ((x + self.__width), (y + self.__width)))

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

    def get_neighbor(self, cells):
        indexes = [self.get_cell(self.x_coordinate, self.y_coordinate - 1),  # top side
                   self.get_cell(self.x_coordinate, self.y_coordinate + 1),  # bottom side
                   self.get_cell(self.x_coordinate - 1, self.y_coordinate),  # left side
                   self.get_cell(self.x_coordinate + 1, self.y_coordinate)]  # right side

        neighbors = []

        for index in indexes:
            if index != -1 and cells[index].visited is False:
                neighbors.append(cells[index])

        if neighbors:
            v = random.choice(neighbors)
            return cells.index(v)
