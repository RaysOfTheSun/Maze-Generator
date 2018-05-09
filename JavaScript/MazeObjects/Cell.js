/**
 * Initializes a new instance of the cell class
 * @param  {int} x_coordinate [The position of the cell relative to the x-axis]
 * @param  {int} y_coordinate [The position of the cell relative to the y-axis]
 * @param  {int} width        [The thickness of the cell]
 * @constructor
 */
function Cell (x_coordinate, y_coordinate, width) {
  this.x_coordinate = x_coordinate;
  this.y_coordinate = y_coordinate;
  this.width = width;
  this.visited = false;
  this.Walls = {};
  this.BuildWalls();
}

/**
 * Initializes each wall of the cell
 */
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

  this.Walls = {"top": top, "bottom": bottom, "right": right, "left": left};
};

/**
 * Draws the cell onto the canvas
 */
Cell.prototype.Draw = function () {
  for (var wall in this.Walls) {
    if (this.Walls[wall].show) {
      stroke(255);
      this.Walls[wall].Draw();
    }
    else{
      noStroke();
      noFill();
    }
  }

  if (this.visited){
    noStroke();
    fill(102, 51, 153, 128);
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

    return x_coordinate + y_coordinate * grid_row_count;
};

/**
 * Gets the next neighbor of the current cell
 * @param  {Array} grid            The collection of cells
 * @param  {Number} [grid_width=10] The number of columns in the grid
 * @return {Cell}                 The next cell to be visited
 */
Cell.prototype.GetNeighbor = function (grid, grid_width = 10) {
  let neighbor_indexes = [
    this.GetNeighborIndex(this.x_coordinate, this.y_coordinate + 1, grid_width),
    this.GetNeighborIndex(this.x_coordinate, this.y_coordinate - 1, grid_width),
    this.GetNeighborIndex(this.x_coordinate + 1, this.y_coordinate, grid_width),
    this.GetNeighborIndex(this.x_coordinate - 1, this.y_coordinate, grid_width)
  ];

  let neighbors = [];

  for (index of neighbor_indexes) {
    if ((index != -1) && (!grid[index].visited)){
      neighbors.push(grid[index]);
    }
  }

  return random(neighbors);
};

/**
 * Draws a rectangle that is the same dimensions as the cell
 * @param  {Number} red   Red value
 * @param  {Number} green Green value
 * @param  {Number} blue  Blue value
 */
Cell.prototype.Highlight = function (red, green, blue, alpha = 128) {
  fill(red, green, blue, alpha);
  rect(this.x_coordinate * this.width, this.y_coordinate * this.width,
    this.width, this.width);
};

/**
 * Removes the wall between the current cell and its neighbor
 * @param  {Cell} neighbor The neighboring cell object
 */
Cell.prototype.RemoveWalls = function (neighbor) {
  if ((neighbor.x_coordinate - this.x_coordinate) == 1){
    this.Walls["right"].show = false;
    neighbor.Walls["left"].show = false;
  }
  else if ((neighbor.x_coordinate - this.x_coordinate) == -1) {
    this.Walls["left"].show = false;
    neighbor.Walls["right"].show = false;
  }
  else if ((this.y_coordinate - neighbor.y_coordinate) == 1) {
    this.Walls["top"].show = false;
    neighbor.Walls["bottom"].show = false;
  }
  else if ((this.y_coordinate - neighbor.y_coordinate) == -1){
    this.Walls["bottom"].show = false;
    neighbor.Walls["top"].show = false;
  }
};
