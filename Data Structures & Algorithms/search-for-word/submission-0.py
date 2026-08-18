class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        stack = []
        if not board:
            return not word
        rowLimit = len(board)
        colLimit = len(board[0])
        visited = [ [0] * colLimit for i in range(rowLimit)]

        def searchBoard(i, j): # i picks the row, j picks the column
            nonlocal stack
            nonlocal visited
            if word == ''.join(stack):
                return True
            if len(stack) > len(word):
                return False
            if i >= rowLimit or i < 0:
                return False
            if j >= colLimit or j < 0:
                return False
            if visited[i][j] == 1:
                return False

            visited[i][j] = 1
            stack.append(board[i][j])
            found = searchBoard(i + 1, j) \
            or searchBoard(i - 1, j) \
            or searchBoard(i, j + 1) \
            or searchBoard(i, j - 1)
            stack.pop()
            visited[i][j] = 0
            return found

        for i in range(rowLimit):
            for j in range(colLimit):
                if searchBoard(i, j):
                    return True

        return False