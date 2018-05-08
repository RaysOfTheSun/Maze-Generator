function PathFinder(x_coordinate, y_coordinate, grid){
  this.x_coordinate = x_coordinate;
  this.y_coordinate = y_coordinate;
  this.open_list = [];
  this.closed_list = [];
  this.maze = grid;
  this.grid = grid.map(cell => new PathFindingCell(cell.x_coordinate,
    cell.y_coordinate));
}


PathFinder.prototype.GetIndex = function (x_coordinate, y_coordinate, grid_width) {
  if (x_coordinate < 0 || y_coordinate < 0 || x_coordinate > grid_width - 1
    || y_coordinate > grid_width - 1) {
      return - 1;
    }
  else {
    return x_coordinate + y_coordinate * grid_width;
  }
};

PathFinder.prototype.PathFind = function (grid_width) {
  let indexes = [
    this.GetIndex(this.x_coordinate, this.y_coordinate + 1, grid_width),
    this.GetIndex(this.x_coordinate, this.y_coordinate - 1, grid_width),
    this.GetIndex(this.x_coordinate + 1, this.y_coordinate, grid_width),
    this.GetIndex(this.x_coordinate - 1, this.y_coordinate, grid_width)
  ];

  let curr_cell = this.grid[this.GetIndex(this.x_coordinate,
    this.y_coordinate, grid_width)];
  // console.log(this.grid[this.grid.length - 1]);
  let target = this.grid[this.grid.length - 1];
  curr_cell.ComputeScore(-1, target);

  // let positions = ["top", "bottom", "left", "right"];

  indexes = indexes.filter(index => index != -1);

  for (let i = 0; i < indexes.length; i++) {
    if (!this.closed_list.includes(this.grid[indexes[i]])
        && !this.open_list.includes(indexes[i])) {
      this.open_list.push(indexes[i]);
    }
  }
  // console.log(this.open_list);
  let chosen = undefined;

  if (this.open_list.length > 0) {
    for (var i = 0; i < this.open_list.length; i++) {
      this.grid[this.open_list[i]].ComputeScore(curr_cell.G_score, target);
      if (this.grid[this.open_list[i]].F_score <= curr_cell.F_score) {
        chosen = this.grid[this.open_list[i]];
      }
    }
  }

  // console.log(chosen);
  if (chosen != undefined) {
    this.x_coordinate = chosen.x_coordinate;
    this.y_coordinate = chosen.y_coordinate;
    this.closed_list.push(chosen);
    this.open_list = [];
  }


};
