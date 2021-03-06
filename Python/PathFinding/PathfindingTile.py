class Tile:
    def __init__(self, coordinates):
        self.x_coordinate, self.y_coordinate = coordinates
        self.g_score, self.h_score, self.f_score = 0, 0, 0
        self.parent = None

    def score(self, previous_tile_g_score, goal):
        """
        Computes for the G, H and F scores of the tile
        :param previous_tile_g_score: (Tile) The parent of this tile
        :param goal: The target tile in the grid
        :return: None
        """
        goal_x_coordinate, goal_y_coordinate = goal
        self.g_score = previous_tile_g_score + 1
        # The H score is computed using the manhattan distance formula: (|x_tar - x_self|) + (|y_tar - y_self|)
        self.h_score = abs((goal_x_coordinate - self.x_coordinate) +
                           (goal_y_coordinate - self.y_coordinate))
        self.f_score = self.g_score + self.h_score





