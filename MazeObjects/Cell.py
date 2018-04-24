import pygame
from MazeObjects.Colors import Color


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
        self.__palette = Color()

    def draw(self, surface):
        """
        draws a square shaped cell on the canvas/screen/whatever
        Each cell is composed of four sides. Each side is an individual line.
        :return: nothing
        """
        x = self.__x_coordinate * self.__width
        y = self.__y_coordinate * self.__width

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

        rectangle = pygame.Surface((self.__width, self.__width))
        rectangle.fill(self.__palette.purple)
        rectangle.set_alpha(50)
        # surface.blit(rectangle, (self.__x_coordinate, self.__y_coordinate))
        surface.blit(rectangle, (0, 0))

    def get_neighbors(self):
        neighbors = []








