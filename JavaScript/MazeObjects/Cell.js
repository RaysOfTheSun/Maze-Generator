/**
 * Initializes a new instance of the cell class
 * @param       {int} x_coordinate [The position of the cell relative to the x-axis]
 * @param       {int} y_coordinate [The position of the cell relative to the y-axis]
 * @param       {int} width        [The thickness of the cell]
 * @constructor
 */
function Cell (x_coordinate, y_coordinate, width) {
  this.x_coordinate = x_coordinate;
  this.y_coordinate = y_coordinate;
  this.width = width;
  this.visited = false;
  this.Walls = [];
  this.BuildWalls();
}

Cell.prototype.BuildWalls = function () {
  let x = this.x_coordinate * this.width;
  let y = this.y_coordinate * this.width;
  let top = new CellWall([x, y],
    [x + this.width, y]);
  let bottom = new CellWall([x, y + this.width],
    [x + this.width, y + this.width])
  let right = new CellWall([x + this.width, y],
    [x + this.width, y + this.width]);
  let left = new CellWall([x, y],
    [x, y + this.width]);

  this.Walls.push(top);
  this.Walls.push(bottom);
  this.Walls.push(right);
  this.Walls.push(left);
};

Cell.prototype.Draw = function () {
  stroke(255);
  for(let i = 0; i < this.Walls.length; i++){
    if (this.Walls[i].show){
      this.Walls[i].Draw();
    }
  }

  if (this.visited){
    fill(102, 51, 153, 158);
    rect(this.x_coordinate * this.width,
      this.y_coordinate * this.width , this.width, this.width);
    }
  };

/**
 * Gets the index a cell in the grid based on its x and y coordinates
 * @param  {int} x_coordinate   The position of the cell relative to the x-axis
 * @param  {int} y_coordinate   The position of the cell relative to the y-axis
 * @param  {int} grid_row_count The number of rows present in the grid
 * @return {int}                The index of the cell in the grid array
 */
Cell.prototype.GetNeighborIndex = function (x_coordinate, y_coordinate, grid_row_count) {
  if ((x_coordinate < 0) || (y_coordinate < 0) || (x_coordinate > grid_row_count - 1)
        || (y_coordinate > grid_row_count - 1)){
          return - 1;
        }
  else {
    return x_coordinate + y_coordinate * grid_row_count - 1;
  }
};

/**
 * Gets the neighbors of a given cell.
 * @return {[type]} [description]
 */
Cell.prototype.GetNeighbors = function () {
  let neighbors = [

  ]
};
