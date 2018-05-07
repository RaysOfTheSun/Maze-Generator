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

  current.visited = true;
  let next = current.GetNeighbor(maze.Cells, floor(width / maze.cell_width));
  maze.visited_cells.push(current);
  current = next;
  // console.log(next);

  // console.log(current);
  // console.log(maze.Cells.length);
}
