class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return False

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)


        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                value = int(board[r][c])
                if value in rows[r]:
                    return False
                elif value in cols[c]:
                    return False
                elif value in squares[(r // 3, c // 3)]:
                    return False

                rows[r].add(value)
                cols[c].add(value)
                squares[(r // 3, c // 3)].add(value)

        return True
