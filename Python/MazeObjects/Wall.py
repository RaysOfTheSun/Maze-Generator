from MazeObjects.Colors import Color  # Maybe I get bored
import pygame


class Wall:
    def __init__(self, start_points, end_points):
        """
        Initializes an instance of the wall class
        :param start_points: The position of the wall on the x-axis
        :param end_points: The position of the wall on the y-axis
        """
        self.show = True
        self.__palette = Color()
        self.__color = self.__palette.white
        self.x_coordinate = start_points
        self.y_coordinate = end_points

    def draw(self, surface):
        """
        Draws a single line using the parameters given to the object during initialization
        :param surface: The canvas in where the line is to be drawn on
        :return: None
        """
        pygame.draw.line(surface, self.__palette.white, self.x_coordinate, self.y_coordinate)
