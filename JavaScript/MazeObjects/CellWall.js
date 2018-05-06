function CellWall (start, end){
  this.show = true;
  this.start = start;
  this.end = end;
}

CellWall.prototype.Draw = function () {
  line(this.start[0], this.start[1], this.end[0], this.end[1]);
};
