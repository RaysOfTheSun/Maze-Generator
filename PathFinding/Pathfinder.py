import pygame
from MazeObjects.Colors import Color
from PathFinding.PathfindingTile import Tile

class Pathfinder:
    def __init__(self, initial_coordinates, goal_coordinates, grid):
        self.x_coordinate, self.y_coordinate = initial_coordinates
        self.x_goal, self.y_goal = goal_coordinates
        self.open_paths, self.closed_paths = [], []
        self.paths = [Tile((cell.x_coordinate, cell.y_coordinate)) for cell in grid]

    def get_neighbors(self, x_coordinate, y_coordinate):
        neighbors = {'top': (x_coordinate, (y_coordinate + 1)), 'bottom': (x_coordinate, (y_coordinate + 1)),
                     'left': ((x_coordinate - 1), y_coordinate), 'right': ((x_coordinate + 1), y_coordinate)}







