function Cell (x_coordinate, y_coordinate, width) {
  this.x_coordinate = x_coordinate;
  this.y_coordinate = y_coordinate;
  this.width = width;
  this.Walls = [];
  this.BuildWalls();
}

Cell .prototype.BuildWalls = function () {
  let wall_coordinates = {'Top':[this.x_coordinate, this.y_coordinate + 1],
                          'bottom': [this.x_coordinate, this.y_coordinate - 1],
                          'left': [this.x_coordinate - 1, this.y_coordinate],
                          'right': [this.x_coordinate + 1, this.y_coordinate]
                        };

};
