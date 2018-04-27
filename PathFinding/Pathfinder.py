import pygame
from MazeObjects.Colors import Color


class Pathfinder:
    def __init__(self, initial_coordinates, goal_coordinates):
        self.x_coordinate, self.y_coordinate = initial_coordinates
        self.x_goal, self.y_goal = goal_coordinates
        self.open_paths, self.closed_paths = [], []

    def get_neighbors(self, x_coordinate, y_coordinate):
        neighbors = {'top': (x_coordinate, (y_coordinate + 1)), 'bottom': (x_coordinate, (y_coordinate + 1)),
                     'left': ((x_coordinate - 1), y_coordinate), 'right': ((x_coordinate + 1), y_coordinate)}






