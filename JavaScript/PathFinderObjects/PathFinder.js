/**
 * Initializes an instance of the PathFinder class
 * @param       {int} x_coordinate The intitial position of the PathFinder
 *                                    relative to the x-axis
 * @param       {int} y_coordinate The intitial position of the PathFinder
 *                                    relative to the y-axis
 * @param       {array} grid       The collection of cells in the PathFinder's
 *                                  enivironment
 * @constructor
 */
function PathFinder(x_coordinate, y_coordinate, grid){
  this.grid = grid.map(cell => new PathFindingCell(cell.x_coordinate, cell.y_coordinate));
  this.maze = grid;
  this.x_coordinate = x_coordinate;
  this.y_coordinate = y_coordinate;
  this.cell = this.grid[0];
  this.target = this.grid[this.grid.length - 1];
  this.cell.ComputeScore(-1, this.target);
  this.open_list = [];
  this.closed_list = [];
}

/**
 * Gets the index a cell in the grid based on its x and y coordinates
 * @param  {int} x_coordinate   The position of the cell relative to the x-axis
 * @param  {int} y_coordinate   The position of the cell relative to the y-axis
 * @param  {int} grid_row_count The number of rows present in the grid
 * @return {int}                The index of the cell in the grid array
 */
PathFinder.prototype.GetNeighborIndex = function (x_coordinate, y_coordinate, grid_row_count) {
  if ((x_coordinate < 0) || (y_coordinate < 0) || (x_coordinate > grid_row_count - 1)
        || (y_coordinate > grid_row_count - 1)){
          return - 1;
        }

    return x_coordinate + y_coordinate * grid_row_count;
};

PathFinder.prototype.IsPassable = function (postion, self, target) {
  // console.log(`target = ${target}`);
  if (postion == "top") {
    if (self.Walls[postion].show && target.Walls["bottom"].show) {
      return true;
    }
  }
  else if (postion == "bottom") {
    if (self.Walls[postion].show && target.Walls["top"].show) {
      return true;
    }
  }
  else if (postion == "left") {
    if (self.Walls[postion].show && target.Walls["right"].show) {
      return true;
    }
  }
  else {
    if (self.Walls[postion].show && target.Walls["left"].show) {
      return true;
    }
  }

  return false;
};

PathFinder.prototype.PathFind = function (grid_width = 10) {
  let neighbor_indexes = {
    "top": this.GetNeighborIndex(this.x_coordinate,
      this.y_coordinate + 1, grid_width),
    "bottom": this.GetNeighborIndex(this.x_coordinate,
      this.y_coordinate - 1, grid_width),
    "left": this.GetNeighborIndex(this.x_coordinate + 1,
      this.y_coordinate, grid_width),
    "right": this.GetNeighborIndex(this.x_coordinate - 1,
      this.y_coordinate, grid_width)
  };

  let tile_index = this.grid.indexOf(this.cell);
  // console.log(`I am the cell ${this.maze[tile_index]}`);
  for(var neighbor_index in neighbor_indexes){
      let index = neighbor_indexes[neighbor_index];
      if (index != -1) {
                // console.log(`I am passable: ${index}`);
          this.grid[index].ComputeScore(this.cell.G_score, this.target);
          this.open_list.push(this.grid[index]);
      }
    }

  // console.log(`I am the cell ${this.cell}`);
    console.log(this.open_list);

  let chosen = undefined;
  if (this.open_list.length > 0) {
    this.open_list.sort((a, b) => a.F_score - b.F_score);
    console.log(`sorted: ${this.open_list}`);
    chosen = this.open_list[0];
    this.closed_list.push(chosen);
    this.open_list = [];
  }

  if (chosen != undefined) {
    let parent = this.cell;
    chosen.Parent = parent;
    this.cell = chosen;

    this.x_coordinate = this.cell.x_coordinate;
    this.y_coordinate = this.cell.y_coordinate;
  }
};
