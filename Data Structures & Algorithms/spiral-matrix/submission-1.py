class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        ROWS, COLS = len(matrix), len(matrix[0])
        t, b = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1
        
        while l <= r and t <= b:
            for i in range(l, r+1):
                res.append(matrix[t][i])

            for i in range(t+1, b+1):
                res.append(matrix[i][r])

            if l == r or t == b:
                break

            for i in range(r-1, l-1, -1):
                res.append(matrix[b][i])

            for i in range(b-1, t, -1):
                res.append(matrix[i][l])

            l += 1
            r -= 1
            t += 1
            b -= 1

        return res
        
