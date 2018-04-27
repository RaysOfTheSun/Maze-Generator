import pygame
from MazeObjects.Colors import Color


class Pathfinder:
    def __init__(self, x_coordinate, y_coordinate):
        """
        Initializes an instance of the Pathfinder class
        :param x_coordinate: The initial position of the pathfinder in the x-axis
        :param y_coordinate: The initial position of the pathfinder in the y-axis
        """
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.closed_paths = []  # Closed list
        self.open_paths = []  # Open list
