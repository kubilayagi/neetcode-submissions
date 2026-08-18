class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(i, j):
            q = deque()
            q.append([i,j])
            while q:
                coords = q.popleft()
                for d in directions:
                    nexti = coords[0] + d[0]
                    nextj = coords[1] + d[1]
                    if 0 <= nexti and nexti < ROWS and 0 <= nextj and nextj < COLS and grid[nexti][nextj] == "1":
                        grid[nexti][nextj] = "0"
                        q.append([nexti, nextj])

        numislands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    bfs(i, j)
                    numislands += 1

        return numislands
