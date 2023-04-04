def ratInAMaze(maze, n):
    # Write your code here.
    path_sets = []
    visited = set()

    def generateSolution(path):
        solution = []
        for x_index in range(len(maze)):
            for y_index in range(len(maze[0])):
                if (x_index, y_index) in path:
                    solution.append("1")
                else:
                    solution.append("0")
        return " ".join(solution)


    def traversal(x_idx, y_idx, path):
        # check for out of bounds 
        if x_idx >= len(maze) or y_idx >= len(maze[0]):
            return
        if x_idx < 0 or y_idx < 0:
            return
        if (x_idx, y_idx) in visited:
            return
        
        # check for blocker 
        if maze[x_idx][y_idx] == 0:
            return
        
        path.append((x_idx, y_idx))

        # check for destination
        if( x_idx == len(maze) - 1) and (y_idx == len(maze[0]) - 1):
            path_sets.append(path.copy())
            path.pop()
            return
        
        visited.add((x_idx, y_idx))
    
        # travsese
        traversal(x_idx + 1, y_idx , path)
        traversal(x_idx, y_idx + 1 , path)
        traversal(x_idx - 1, y_idx , path)
        traversal(x_idx, y_idx - 1, path)
        path.pop()
        visited.pop()

    traversal(0, 0, [])
    result = list(map(generateSolution, path_sets))
    for r in result:
        print(r)




# Main.
n = 3
maze = [[1, 0, 1], [1, 1, 1],  [1, 1, 1]]
ratInAMaze(maze , n)