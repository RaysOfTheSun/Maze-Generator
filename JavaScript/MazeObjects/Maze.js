/**
 * Initializes an instance of the Maze class
 * @param       {Number} cell_width  The width of each cell in the grid
 * @param       {Number} grid_width  The number of columns in the grid
 * @param       {Number} grid_height The number of rows in the grid
 * @constructor
 */
function Maze(cell_width, grid_width, grid_height) {
  this.columns = floor(grid_height/cell_width);
  this.rows = floor(grid_width/cell_width);
  this.cell_width = cell_width;
  this.Cells = [];
  this.visited_cells = [];

  this.Initialize();
}

/**
 * Initializes each cell in the grid
 */
Maze.prototype.Initialize = function () {
  for(let row = 0; row < this.rows; row++){
    for(let column = 0; column < this.columns; column++){
      cell = new Cell(column, row, this.cell_width);
      this.Cells.push(cell);
    }
  }
};

/**
 * Draws the grid of cells onto the canvas
 */
Maze.prototype.Draw = function () {
  for (let i = 0; i < this.Cells.length; i++){
    this.Cells[i].Draw();
  }
};
