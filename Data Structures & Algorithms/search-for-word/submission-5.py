class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = [[False] * COLS for _ in range(ROWS)]
        def dfs(r, c, part):
            if visited[r][c]:
                return False
            if part == word:
                return True
            visited[r][c] = True
            for dr, dc in [[1,0],[-1,0],[0,1],[0,-1]]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    continue
                if dfs(nr, nc, part + board[nr][nc]):
                    return True
            visited[r][c] = False
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, word[0]):
                        return True

        return False

                
            
            