class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxSize = 0

        def bfs(r, c) -> int:
            q = deque()
            q.append((r, c))
            islandSize = 0

            while q:
                row, col = q.popleft()
                if grid[row][col] == 0:
                    continue
                grid[row][col] = 0
                islandSize += 1

                for dr, dc in [[1,0], [-1,0], [0,1], [0,-1]]:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == 0:
                        continue
                    q.append((nr, nc))

            return islandSize

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    s = bfs(r, c)
                    maxSize = max(maxSize, s)

        return maxSize