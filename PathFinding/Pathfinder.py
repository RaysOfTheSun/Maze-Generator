import pygame
from MazeObjects.Colors import Color
from PathFinding.PathfindingTile import Tile


class Pathfinder:
    def __init__(self, initial_coordinates, goal_coordinates, grid):
        self.x_coordinate, self.y_coordinate = initial_coordinates
        self.x_goal, self.y_goal = goal_coordinates
        self.open_paths, self.closed_paths = [], []
        self.paths = [Tile((cell.x_coordinate, cell.y_coordinate)) for cell in grid]

    def walk(self, x_coordinate, y_coordinate):
        """
        Obtains the current cell's neighbors based on its position on the grid then moves the pathfinder
        to the tile with the lowest F score
        :param x_coordinate: The point representing the position of the target tile in the x-axis of the grid
        :param y_coordinate: The point representing the position of the target tile in the y-axis of the grid
        :return:
        """
        neighbors = {'top': (x_coordinate, (y_coordinate + 1)), 'bottom': (x_coordinate, (y_coordinate + 1)),
                     'left': ((x_coordinate - 1), y_coordinate), 'right': ((x_coordinate + 1), y_coordinate)}

        for neighbor in neighbors:
            # Obtain the cell represented by each of the coordinates then compute their scores
            neighbor_x, neighbor_y = neighbors[neighbor]
            curr_neighbor = self.paths[neighbor_x + neighbor_y * (len(self.paths) // 10)]
            curr_neighbor.compute_scores((self.x_goal, self.y_goal))
            self.open_paths.append(curr_neighbor)

        self.open_paths.sort(key=lambda n: n.F_score, reverse=True)  # sort the list by F score in ascending order

        return self.open_paths[0]
