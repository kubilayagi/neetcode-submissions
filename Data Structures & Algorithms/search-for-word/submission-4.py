class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ROWS, COLS = len(board), len(board[0])
        visited = [[False] * len(board[0]) for _ in range(len(board))]

        def dfs(r, c, wrd) -> bool:
            nonlocal visited
            if wrd == "":
                return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or visited[r][c] or board[r][c] != str(wrd[0]):
                return False
            visited[r][c] = True
            res = (
                dfs(r + 1, c, wrd[1:]) or
                dfs(r - 1, c, wrd[1:]) or
                dfs(r, c + 1, wrd[1:]) or
                dfs(r, c - 1, wrd[1:])
            )
            visited[r][c] = False
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == str(word[0]):
                    if dfs(r, c, word):
                        return True

        return False