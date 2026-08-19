class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        
        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = "0"

            while q:
                row, col = q.popleft()
                for dr, dc in [[1,0], [-1,0], [0,1], [0,-1]]:
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == "0"):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands