function Cell (x_coordinate, y_coordinate, width) {
  this.x_coordinate = x_coordinate;
  this.y_coordinate = y_coordinate;
  this.width = width;
  this.visited = false;
  this.Walls = [];
  this.BuildWalls();
}

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

  this.Walls.push(top);
  this.Walls.push(bottom);
  this.Walls.push(right);
  this.Walls.push(left);
  }

  Cell.prototype.Draw = function () {
    stroke(255);
    for(let i = 0; i < this.Walls.length; i++){
      if (this.Walls[i].show){
        this.Walls[i].Draw();
      }
    }

    if (this.visited){
      fill(102, 51, 153, 128);
      rect(this.x_coordinate * this.width,
        this.y_coordinate * this.width , this.width, this.width);
    }
  };
