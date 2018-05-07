function Maze(cell_width, grid_width, grid_height) {
  this.columns = floor(grid_height/cell_width);
  this.rows = floor(grid_width/cell_width);
  this.cell_width = cell_width;
  this.Cells = [];
  this.visited_cells = [];

  this.Initialize();
}

Maze.prototype.Initialize = function () {
  for(let row = 0; row < this.rows; row++){
    for(let column = 0; column < this.columns; column++){
      cell = new Cell(column, row, this.cell_width);
      this.Cells.push(cell);
    }
  }
};

Maze.prototype.Draw = function () {
  for (let i = 0; i < this.Cells.length; i++){
    this.Cells[i].Draw();
  }
};
