function CellWall (start, end){
  this.show = false;
  this.start = start;
  this.end = end;
}

CellWall.prototype.Build = function () {
  line(start[0], start[1], end[0], end[1]);
}
