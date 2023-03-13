def isSafe( maze, x, y,N ):
	
	
	if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1:
		return True
	
	return False

def printSolution( sol ):
     
    for i in sol:
        for j in i:
            print(str(j) + " ", end ="")
        print("")

def solveMaze( maze,N ):
	sol = [ [ 0 for j in range(N) ] for i in range(N) ]
	
	if solveMazeUtil(maze, 0, 0, sol,N) == False:
		print("Solution doesn't exist");
		return False
	printSolution( sol )
	return True
	

def solveMazeUtil(maze, x, y, sol,N):
	if x == N - 1 and y == N - 1:
		sol[x][y] = 1
		return True
	if isSafe(maze, x, y,N) == True:
		sol[x][y] = 1
		if solveMazeUtil(maze, x + 1, y, sol,N) == True:
			return True
		if solveMazeUtil(maze, x, y + 1, sol,N) == True:
			return True
		sol[x][y] = 0
		return False


