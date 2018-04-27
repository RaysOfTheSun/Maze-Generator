class Tile:
    def __init__(self, coordinates):
        """
        Initializes an instance of the Tile class
        :param coordinates: The position of the tile in the grid (Tuple)
        """
        self.G_Score = -1
        self.H_Score = -1
        self.F_Score = -1
        self.x_coordinates, self.y_coordinates = coordinates

    def compute_estimate(self, coordinates):
        """
        Computes the H score for the tile
        The H score is the distance from the cell to the target cell disregarding obstacles
        :param coordinates: The coordinates of the target cell in the grid (Tuple)
        :return: The H score of the tile relative to the target cell
        """
        goal_x, goal_y = coordinates
        return abs(((goal_x - self.x_coordinates) + (goal_y - self.y_coordinates)))  # Manhattan Distance Formula




