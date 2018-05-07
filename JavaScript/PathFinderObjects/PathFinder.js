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
  this.grid = grid.map((cell => new PathFindingCell(cell.x_coordinate,
    cell.y_coordinate)));
  this.x_coordinate = x_coordinate;
  this.y_coordinate = y_coordinate;
  // The x or y coordinates of the last cell in the grid is the same as
  // the total number of rows and columns in the grid. So, we can pass that
  // number to the method.
  this.cell = this.grid[this.GetNeighborIndex(x_coordinate, y_coordinate,
                                this.grid[this.grid.length].x_coordinate)]
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

PathFinder.prototype.GetNeighbor = function () {

};
