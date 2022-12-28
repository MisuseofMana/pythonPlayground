gridSize = int(input("How many rows and columns for the maze?: "))

def init_maze(width, height):
    maze = []
    for i in range(0, height):
        line = []
        for j in range(0, width):
            line.append('u')
        maze.append(line)    
return maze

init_maze(gridSize, gridSize)