class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))
            while q:
                row, col = q.popleft()
                for d in directions:
                    nr, nc = row + d[0], col + d[1]
                    if 0 <= nr and nr < ROWS and 0 <= nc and nc < COLS and grid[nr][nc] == "1":
                        q.append((nr, nc))
                        grid[nr][nc] = "0"

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1

        return islands

                