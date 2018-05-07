var maze = undefined;
var current = undefined;

function setup(){
  createCanvas(800, 800);
  maze = new Maze(20, width, height);
  current = maze.Cells[0];
}

function draw(){
  frameRate(15);
  background(51);
  maze.Draw();
  current.Highlight(255, 255, 0);
  current.visited = true;
  let next = current.GetNeighbor(maze.Cells, floor(width / maze.cell_width));
  if (next != undefined) {
    maze.visited_cells.push(current);
    current = next;
  }
  else {
    current = maze.visited_cells.pop();
  }
}
