/**
 * Initializes an instance o fthe PathFinderCell class
 * @param       {int} x_coordinate The position of the PathFinderCell
 *                relative to the x-axis
 * @param       {int} y_coordinate The position of the PathFinderCell
 *                relative to the y-axis
 * @constructor
 */
function PathFindingCell(x_coordinate, y_coordinate){
  this.x_coordinate, this.y_coordinate = x_coordinate, y_coordinate;
  this.G_score, this.F_score, this.H_score = 0, 0, 0;
}

PathFinderCell.prototype.ComputeScore = function (parent_g_score, target) {
  this.G_score = parent_g_score + 1;
  this.H_score = abs((target.x_coordinate - this.x_coordinate)) +
            abs((target.y_coordinate - this.y_coordinate));
  this.F_score = this.G_score + this.H_score;
};
