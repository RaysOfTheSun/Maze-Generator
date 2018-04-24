import pygame
from MazeObjects.Colors import Color as Color


class Cell:
    def __init__(self, x_coordinate, y_coordinate, width):
        """
        Creates an instance of the cell class
        :param x_coordinate:
        :param y_coordinate: 
        :param width: How wide and tall the cell would be.
        """
        self.__x_coordinate = x_coordinate
        self.__y_coordinate = y_coordinate
        self.__width = width
        self.visited = False
        self.walls = [True, True, True, True]

    def draw(self, surface):
        """
        draws a square shaped cell on the canvas/screen/whatever
        Each cell is composed of four sides. Each side is an individual line.
        :return: nothing
        """
        x = self.__x_coordinate * self.__width
        y = self.__y_coordinate * self.__width

        # draw upper side of the cell
        pygame.draw.line(surface, Color.white, (x, y), ((x + self.__width), y))
        # draw the bottom side of the cell
        pygame.draw.line(surface, Color.white, (x, y + self.__width), ((x + self.__width), y + self.__width))
        # draw the left side of the cell
        pygame.draw.line(surface, Color.white, (x, y), ((x + self.__width), y + self.__width))
        # draw the right side of the cell
        pygame.draw.line(surface, Color.white, ((x + self.__width), y), ((x + self.__width), y + self.__width))

