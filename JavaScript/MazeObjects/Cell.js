function Cell (x_coordinate, y_coordinate, width) {
  this.x_coordinate = x_coordinate;
  this.y_coordinate = y_coordinate;
  this.width = width;
  this.Walls = [];
  this.BuildWalls();
}

Cell .prototype.BuildWalls = function () {
  let top = new CellWall([this.x_coordinate, this.y_coordinate],
    [this.x_coordinate + this.width, this.y_coordinate]);
  let bottom = new CellWall([this.x_coordinate, this.y_coordinate + this.width],
    [this.x_coordinate + this.width, this.y_coordinate + this.width])
  let right = new CellWall([this.x_coordinate + this.width, this.y_coordinate],
    [this.x_coordinate + this.width, this.y_coordinate + this.width]);
  let left = new CellWall([this.x_coordinate, this.y_coordinate],
    [this.x_coordinate, this.y_coordinate + this.width]);

  this.Walls.push(top);
  this.Walls.push(bottom);
  this.Walls.push(right);
  this.Walls.push(left);

  }
