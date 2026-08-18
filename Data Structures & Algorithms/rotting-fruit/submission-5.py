class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        ROWS = len(grid)
        COLS = len(grid[0])
        startrow, startcol = -1, -1
        fresh = 0

        q = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if not q:
            return -1 if fresh > 0 else 0

        def bfs(sr, sc) -> int:
            nonlocal q
            nonlocal grid
            nonlocal fresh
            res = 0
            directions = [[-1,0], [1,0], [0,1], [0,-1]]
            while q:
                cur = q.popleft()
                r = cur[0]
                c = cur[1]
                level = cur[2]
                if grid[r][c] == 1:
                    res = max(res, level)
                    fresh -= 1
                grid[r][c] = -1 # mark visited
                for d in directions:
                    nr = r + d[0]
                    nc = c + d[1]
                    if nr < ROWS and nr >= 0 and nc < COLS and nc >= 0:
                        if grid[nr][nc] == 1:
                            q.append((nr, nc, level + 1))
            return res if fresh == 0 else -1

        return bfs(startrow, startcol)
