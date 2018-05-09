function PathFinder(x_coordinate, y_coordinate, grid){
  this.x_coordinate = x_coordinate;
  this.y_coordinate = y_coordinate;
  this.open_list = [];
  this.closed_list = [];
  this.maze = grid;
  this.grid = grid.map(cell => new PathFindingCell(cell.x_coordinate,
    cell.y_coordinate));
  this.curr_cell = this.grid[this.GetIndex(this.x_coordinate,
    this.y_coordinate, this.grid[this.grid.length - 1].x_coordinate)];
  this.goal = this.grid[this.grid.length - 1];
  this.curr_cell.ComputeScore(-1, this.goal);
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

PathFinder.prototype.IsPassable = function (x_coordinate, y_coordinate, grid_width) {
  let cur = this.maze[this.x_coordinate + this.y_coordinate * grid_width].Walls;
  let neighbor = this.maze[x_coordinate + y_coordinate * grid_width].Walls;
  let n = this.maze[x_coordinate + y_coordinate * grid_width];
  // n.Highlight(255, 255, 255);
  // console.log(neighbor);
  if ((x_coordinate - this.x_coordinate) == 1) {
    if (!cur["right"].show && !neighbor["left"].show){
      return true;
    }
  }
  else if ((x_coordinate - this.x_coordinate) == -1){
    if (!cur["left"].show && !neighbor["right"].show){
      return true;
    }
  }
  else if ((this.y_coordinate - y_coordinate) == 1) {
    if (!cur["top"].show && !neighbor["bottom"].show){
      return true;
    }
  }
  else {
    if (!cur["bottom"].show && !neighbor["top"].show){
      return true;
    }
  }

  // return false;
};


PathFinder.prototype.PathFind = function (grid_width) {
  let indexes = [
    this.GetIndex(this.x_coordinate, this.y_coordinate + 1, grid_width),
    this.GetIndex(this.x_coordinate, this.y_coordinate - 1, grid_width),
    this.GetIndex(this.x_coordinate + 1, this.y_coordinate, grid_width),
    this.GetIndex(this.x_coordinate - 1, this.y_coordinate, grid_width)
  ];




  indexes = indexes.filter(index => index != -1 && index != 0);

  for (let i = 0; i < indexes.length; i++) {
    if (!this.closed_list.includes(this.grid[indexes[i]])
        && !this.open_list.includes(indexes[i])) {
      this.open_list.push(indexes[i]);
    }
  }

  this.open_list = this.open_list.filter(index => index != -1);
  // console.log(this.open_list);

  let neighbors = [];

  for (let i = 0; i < this.open_list.length; i++) {
    let n = this.grid[this.open_list[i]];
    if (!neighbors.includes(this.grid[this.open_list[i]])
        && this.IsPassable(n.x_coordinate, n.y_coordinate, grid_width)) {
          n.ComputeScore(this.curr_cell.G_score, this.goal);
          neighbors.push(n);
    }
  }

  // neighbors = neighbors.sort((a, b) => a.F_score - b.F_score);

  // console.log(neighbors);

  let chosen = undefined;

  if (neighbors.length > 0) {
    chosen = neighbors[0];
  }

  // if (this.open_list.length > 0) {
  //   for (var i = 0; i < this.open_list.length; i++) {
  //     let nei = this.maze[this.open_list[i]];
  //     this.grid[this.open_list[i]].ComputeScore(this.curr_cell.G_score, this.goal);
  //     if (this.grid[this.open_list[i]].F_score <= this.curr_cell.F_score
  //       && this.IsPassable(nei.x_coordinate, nei.y_coordinate, grid_width)) {
  //         // console.log(nei);
  //         chosen = this.grid[this.open_list[i]];
  //     }
  //   }
  // }

  // console.log(chosen);
  if (chosen != undefined) {
    this.x_coordinate = chosen.x_coordinate;
    this.y_coordinate = chosen.y_coordinate;
    this.curr_cell = chosen;
    this.closed_list.push(chosen);
    this.open_list = [];
  }
  else {

  }


};
