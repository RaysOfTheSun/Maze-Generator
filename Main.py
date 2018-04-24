from MazeObjects.Cell import Cell
import pygame

surface_height, surface_width = 400, 400  # The dimensions of our py game window (height, width)
cell_width = surface_width // 10  # The width of our square shaped cell
grid = []

pygame.init()
surface = pygame.display.set_mode((surface_height, surface_width))
pygame.display.set_caption('Maze Generator')
while True:
    user_action = pygame.event.poll()

    if user_action.type == pygame.QUIT:
        pygame.quit()
        break

    for row in range(cell_width):
        for column in range(cell_width):
            grid_cell = Cell(row, column, cell_width)
            grid.append(grid_cell)
            grid_cell.draw(surface)

    pygame.display.flip()  # update the canvas so the grid will be shown after it is drawn

