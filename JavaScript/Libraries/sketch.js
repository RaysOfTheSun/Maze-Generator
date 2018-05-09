var maze = undefined;
var current = undefined;
var pathfinder = undefined;
var isPathFinding = false;

function setup(){
  createCanvas(800, 800);
  maze = new Maze(20, width, height);
  current = maze.Cells[0];
  pathfinder = new PathFinder(0, 0, maze.Cells);
}

function draw(){
  frameRate(240);
  background(51);
  maze.Draw();

  current.Highlight(255, 255, 0);
  current.visited = true;
  let next = current.GetNeighbor(maze.Cells, floor(width / maze.cell_width));

  if (next != undefined) {
    maze.Cells[maze.Cells.indexOf(current)].RemoveWalls(next);
    maze.visited_cells.push(current);
    current = next;
  }
  else if (maze.visited_cells.length != 0){
    current = maze.visited_cells.pop();
  }
  else { // Means we're done building the maze for the pathfinder to use
  frameRate(15);
    current = maze.Cells[pathfinder.x_coordinate + pathfinder.y_coordinate * maze.columns];
    if (current != maze.Cells[maze.Cells.length - 1]){
      // console.log('yay');
      pathfinder.PathFind(maze.rows);
    }
  }
}
