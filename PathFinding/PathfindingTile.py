class Tile:
    def __init__(self, coordinates):
        """
        Initializes an instance of the Tile class
        :param coordinates: The position of the tile in the grid (Tuple)
        """
        self.G_Score = 0
        self.H_Score = 0
        self.F_Score = 0
        self.x_coordinates, self.y_coordinates = coordinates

    def compute_scores(self, goal_coordinates, previous_cell):
        """
        Computes the H score for the tile
        The H score is the distance from the cell to the target cell disregarding obstacles
        :param goal_coordinates: The coordinates of the target cell in the grid (Tuple)
        :param previous_cell: The cell where this cell was based on
        :return: The H score of the tile relative to the target cell
        """
        goal_x, goal_y = goal_coordinates
        self.H_Score = abs(((goal_x - self.x_coordinates) +
                            (goal_y - self.y_coordinates)))  # Manhattan Distance Formula

        self.G_Score = previous_cell.G_score + 1
        self.F_Score = self.F_Score + self.G_Score  # The F score is the overall score of the tile







