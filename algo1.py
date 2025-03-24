'''
Algorithm 1: Walls of Maria
Author: Chris Alpuerto
CSUF email: calpuerto@csu.fullerton.edu
Submission: Project 2

'''
from collections import deque

class WallsOfMaria:
    def SafeCity(self, grid):
        '''
        -1 = titan infested area that is impoassable
        0 = safe stronghold that can take refuge
        INF = An open city where humans are trying to survive
        
        '''
        rows = len(grid)
        col = len(grid[0])
        queue = deque()
        # step 1: endque all cells with val 0
        for i in range(rows):
            for j in range(col):
                if grid[i][j] == 0:
                    queue.append((i,j))
        # initialize directions
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        while queue:
            (x,y) = queue.popleft()
            for dx, dy in directions:
                newX = x + dx
                newY = y + dy
                # skip if out of bounds or not open area
                if newX < 0 or newX >= rows or newY < 0 or newY >= col:
                    continue
                if grid[newX][newY] != "INF":
                    continue
                grid[newX][newY] = grid[x][y] + 1
                queue.append((newX, newY))
        return grid
'''
EFFICIENCY ANALYSIS:
This algorithm uses a BFS traversal to calculate the distance from the safe stronghold to the open city.
The time complexity is O(N*M) where N is the number of rows and M is the number of columns in the grid.
The space complexity is O(N*M) as we use a queue to store the cells to be processed.

'''

def main():
    input_grid1 = [
    ["INF", -1, 0, "INF"],
    ["INF", "INF", "INF", -1],
    ["INF", -1, "INF", -1],
    [0, -1, "INF", "INF"]
    ]
    print(f"Welcome to the Walls of Maria and the Titans, where we will keep humanity safe from the Titans!\n"
          "We will demonstrate this algorithm by using the following input grid: \n"
          f"{input_grid1}")
    walls = WallsOfMaria()
    res_grid1 = walls.SafeCity(input_grid1)
    print(res_grid1)

    print("As we can see, the algorithm has successfully calculated the distance from the safe stronghold to the open city.\n")
    input_grid2 = [
        [0, "INF", "INF"],
        ["INF", -1, "INF"],
        ["INF", "INF", 0]
    ]

    print(f"Now let's try another input grid: \n {input_grid2}\n")
    res_grid2 = walls.SafeCity(input_grid2)
    print(f"Let's see the result: ")
    print(f"{res_grid2}\n")
    print("As we can see, the algorithm has successfully calculated the distance from the safe stronghold to the open city with another input grid.\n")

if __name__ == "__main__":
    main()





