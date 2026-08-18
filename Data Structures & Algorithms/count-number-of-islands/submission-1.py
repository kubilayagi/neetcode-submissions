class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        if not grid or not grid[0]:
            return 0
        ROWS = len(grid)
        COLS = len(grid[0])
        islands = 0
        gridcopy = grid.copy()

        def bfs(i, j):
            nonlocal gridcopy
            q = [[i, j]]
            gridcopy[i][j] = "0"
            while q:
                nextcoords = q.pop()
                for d in directions:
                    nexti = nextcoords[0] + d[0]
                    nextj = nextcoords[1] + d[1]
                    if nexti >= 0 and nexti < ROWS and nextj >= 0 and nextj < COLS and grid[nexti][nextj] == "1":
                        grid[nexti][nextj] = "0"
                        q.append([nexti, nextj])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(i, j)
                    islands += 1

        print(grid)


        return islands