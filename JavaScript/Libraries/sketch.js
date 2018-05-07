var maze = undefined;
var current = undefined;

function setup(){
  createCanvas(800, 800);
  maze = new Maze(20, width, height);
  current = maze.Cells[0];
  current.visited = true;
}

function draw(){
  frameRate(60);
  background(51);
  maze.Draw();
  // current = maze.Cells[(current.x_coordinate + 1) + (current.y_coordinate) * floor(width/20)];
  current.visited = true;
}
