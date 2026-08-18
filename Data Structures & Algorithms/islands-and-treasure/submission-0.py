class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return None
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque() # tuple of 3 values - row, col, level
        
        def bfs(r, c):
            nonlocal grid
            visited = [[False] * COLS for _ in range(ROWS)]
            level = 0
            q.append((r, c, level))
            while q:
                curcoords = q.popleft()
                currow = curcoords[0]
                curcol = curcoords[1]
                curlevel = curcoords[2]
                grid[currow][curcol] = min(curlevel, grid[currow][curcol])
                visited[currow][curcol] = True
                for d in directions:
                    checkrow = currow + d[0]
                    checkcol = curcol + d[1]
                    if checkrow >= 0 and checkrow < ROWS and checkcol >= 0 and checkcol < COLS:
                        if grid[checkrow][checkcol] == -1:
                            continue
                        elif visited[checkrow][checkcol]:
                            continue
                        else:
                            q.append((checkrow, checkcol, curlevel + 1))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    bfs(i, j)

        return



'''
The below implementation
1 wouldn't work well because you should be using bfs
2 is o((m * n)^2) even if you did it correctly


def dfs(i, j) -> int:
            nonlocal grid
            nonlocal q
            shortestPath = 2147483647
            q.append([i, j, 0]) # row position, col position, cur depth
            while q:
                coords = q.pop()
                for di, dj in directions:
                    ci = coords[0] + di
                    cj = coords[1] + dj
                    cdepth = coords[2]
                    if ci >= 0 and cj >= 0 and ci < ROWS and cj < COLS:
                        if grid[ci][cj] == -1:
                            continue
                        elif grid[ci][cj] == 0:
                            shortestPath = min(shortestPath, cdepth)
                        else:
                            q.append()
            return shortestPath

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0 or grid[i][j] == -1:
                    continue
                shortest = dfs(i, j)
                grid[i][j] = shortest
'''