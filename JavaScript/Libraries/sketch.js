var maze = undefined;

function setup(){
  createCanvas(600, 600);
  maze = new Maze(20, width, height);
}

function draw(){
  background(51);
  maze.Draw();
}
