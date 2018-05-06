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
        self.tile.score(-1, (9, 9))

    def is_passable(self, position, target):
        """
        Checks if the pathfinder's chosen neighbor is not barricaded by walls
        :param position: The directional position of the chosen neighbor
        :param target: The
        :return:
        """
        curr = self.x_coordinate + self.y_coordinate * 10
        if position is 'bottom':
            if self.maze[curr].walls[position].show is True and \
                    self.maze[target].walls['top'].show is True:
                    return True
        elif position is 'top':
            if self.maze[curr].walls[position].show is True and \
                    self.maze[target].walls['bottom'].show is True:
                    return True
        elif position is 'right':
            if self.maze[curr].walls[position].show is True and \
                    self.maze[target].walls['left'].show is True:
                    return True
        else:
            if self.maze[curr].walls[position].show is True and \
                    self.maze[target].walls['right'].show is True:
                    return True

        return False

    def path_find(self):
        """
        Makes the path finder find the best path to the target
        :return: None
        """
        neighbors = {'top': (self.x_coordinate, self.y_coordinate - 1),
                     'bottom': (self.x_coordinate, self.y_coordinate + 1),
                     'left': (self.x_coordinate - 1, self.y_coordinate),
                     'right': (self.x_coordinate + 1, self.y_coordinate)}

        for neighbor in neighbors:
            coordinates = neighbors[neighbor]
            neighbor_idx = coordinates[0] + coordinates[1] * 10
            if coordinates[0] < 0 or coordinates[1] < 0 or neighbor_idx > 99\
                    or coordinates[0] > 9 or coordinates[1] > 9\
                    or self.is_passable(neighbor, neighbor_idx) \
                    or self.grid[neighbor_idx] in self.closed_list:
                continue

            curr = self.grid[neighbor_idx]
            curr.score(self.tile.g_score, (self.goal_x_coordinate, self.goal_y_coordinate))
            self.open_list.append(curr)

        # sort the tiles in the open list by f score in ascending order
        # so we always get the tile with the smallest possible f score
        self.open_list.sort(key=lambda n: n.f_score)

        if self.open_list:
            chosen = self.open_list[0]
            parent = self.tile
            chosen.parent = parent
            self.tile = chosen
            self.x_coordinate, self.y_coordinate = chosen.x_coordinate, chosen.y_coordinate
            self.closed_list.append(chosen)
            self.open_list.clear()
        else:
            chosen = self.tile.parent
            self.tile = chosen
            self.x_coordinate, self.y_coordinate = chosen.x_coordinate, chosen.y_coordinate