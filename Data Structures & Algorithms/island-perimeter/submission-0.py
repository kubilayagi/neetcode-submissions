class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        if not grid or not grid[0]:
            return 0
        ROWS = len(grid)
        COLS = len(grid[0])

        perimeter = 0

        for i in range(ROWS):
            for j in range(COLS):
                sides = 4
                if grid[i][j] == 0:
                    continue
                for d in directions:
                    checkrow = i + d[0]
                    checkcol = j + d[1]

                    if checkrow >= 0 and checkrow < ROWS and checkcol >= 0 and checkcol < COLS:
                        if grid[checkrow][checkcol] == 1:
                            sides -= 1

                perimeter += sides

        return perimeter

