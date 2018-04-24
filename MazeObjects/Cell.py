import pygame


class Cell:
    def __init__(self, x_coordinate, y_coordinate, width):
        self.__x_coordinate = x_coordinate
        self.__y_coordinate = y_coordinate
        self.__width = width
        self.visited = False

    def draw(self, surface):
        """
        draws a square shaped cell on the canvas/screen/whatever
        Each cell is composed of four sides. Each side is an individual line.
        :return: nothing
        """
        # draw upper part of the cell
        pygame.draw.rect(surface, )
