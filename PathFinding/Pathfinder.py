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
        neighbors = {'top': (self.x_coordinate, self.y_coordinate + 1),
                     'bottom': (self.x_coordinate, self.y_coordinate + 1),
                     'left': (self.x_coordinate - 1, self.y_coordinate),
                     'right': (self.x_coordinate + 1, self.y_coordinate)}

        for neighbor in neighbors:
            coordinates = neighbors[neighbor]
            neighbor_idx = coordinates[1] + coordinates[0] * 10
            if (coordinates[0] < 0) or (coordinates[1] < 0) or (coordinates[0] > 9) or (coordinates[1] > 9)\
                    or (neighbor_idx < 0):
                continue
            elif self.grid[neighbor_idx] in self.closed_list:
                continue
            elif self.maze[self.grid.index(self.tile)].walls[neighbor].show is True:
                current = self.grid[neighbor_idx]
                current.score(self.tile.g_score, self.grid[99])
                if current not in self.closed_list:
                    self.open_list.append(current)

            if self.open_list:
                self.open_list.sort(key=lambda tile: tile.f_score, reverse=True)

                chosen = self.open_list[0]
                self.tile = chosen
                self.x_coordinate, self.y_coordinate = (chosen.x_coordinate, chosen.y_coordinate)
                self.closed_list.append(chosen)
