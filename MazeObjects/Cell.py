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
            rectangle = pygame.Surface((self.__width, self.__width))
            rectangle.fill(self.__palette.purple)
            rectangle.set_alpha(50)
            surface.blit(rectangle, (x, y))

    def highlight(self, surface):
        x = self.x_coordinate * self.__width
        y = self.y_coordinate * self.__width
        rectangle = pygame.Surface((self.__width, self.__width))
        rectangle.fill(self.__palette.green)
        rectangle.set_alpha(255)
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
            if index != -1:
                if not cells[index].visited:
                    neighbors.append(cells[index])

        if neighbors:
            v = random.choice(neighbors)
            cx, cy = v.x_coordinate, v.y_coordinate
            idx = cx + cy * 10
            if not cells[idx].visited:
                return idx  # Since I have to modify the actual list, I have to get the index
            # of the item then modify it from the calling environment. This will do for now

        return None
