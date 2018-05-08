var maze = undefined;
var current = undefined;
var pathfinder = undefined;
var isPathFinding = false;

function setup(){
  createCanvas(800, 800);
  maze = new Maze(80, width, height);
  current = maze.Cells[0];
  pathfinder = new PathFinder(0, 0, maze.Cells);
}

function draw(){
  frameRate(240);
  background(51);
  maze.Draw();

  if (current != undefined){
    current.Highlight(255, 255, 0);
    current.visited = true;
    let next = current.GetNeighbor(maze.Cells, floor(width / maze.cell_width));

    if (next != undefined) {
      current.RemoveWalls(next);
      maze.visited_cells.push(current);
      current = next;
    }
    else {
      current = maze.visited_cells.pop();
    }
  }
  else { // Means we're done building the maze for the pathfinder to use
  frameRate(15);
    if (maze.Cells.indexOf(current) != maze.Cells.length - 1) {
      isPathFinding = true;
      let ptfndr = maze.Cells[pathfinder.x_coordinate + pathfinder.y_coordinate * maze.columns];
      current = ptfndr;
      current.Highlight(255, 255, 255);
      pathfinder.PathFind(maze.columns);
    }
  }
}
