import pygame
from MazeObjects.Colors import Color
from PathFinding.PathfindingTile import Tile


class Pathfinder:
    def __init__(self, grid, goal):
        self.x_coordinate, self.y_coordinate = 0, 0
        self.goal_x_coordinate, self.goal_y_coordinate = goal
        self.open_list, self.closed_list = [], []
        self.maze = grid
        self.grid = [Tile((cell.x_coordinate, cell.y_coordinate)) for cell in grid]
        self.tile = self.grid[0]

    def walk(self):
        neighbors = {'top': (self.x_coordinate, self.y_coordinate - 1),
                     'bottom': (self.x_coordinate, self.y_coordinate + 1),
                     'left': (self.x_coordinate - 1, self.y_coordinate),
                     'right': (self.x_coordinate + 1, self.y_coordinate)}

        for neighbor in neighbors:
            coordinates = neighbors[neighbor]
            neighbor_idx = coordinates[0] + coordinates[1] * 10
            if coordinates[0] < 0 or coordinates[1] < 0 or neighbor_idx > 99:
                continue
            else:
                curr = self.grid[neighbor_idx]
                curr.score(self.tile.g_score, (self.goal_x_coordinate, self.goal_y_coordinate))
                self.open_list.append(curr)

        self.open_list.sort(key=lambda n: n.f_score)

        chosen = self.open_list[0]
        self.tile = chosen
        self.x_coordinate, self.y_coordinate = chosen.x_coordinate, chosen.y_coordinate
        self.open_list.clear()
