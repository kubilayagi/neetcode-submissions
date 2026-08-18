class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        ROWS, COLS = len(matrix), len(matrix[0])
        t, b = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1
        visited = 0
        total = ROWS * COLS

        while visited < total:
            # l to r (inclusive)
            for i in range(l, r + 1):
                res.append(matrix[t][i])
                visited += 1
            if visited == total:
                break
            # t + 1 to b (inclusive)
            for i in range(t + 1, b + 1):
                res.append(matrix[i][r])
                visited += 1
            if visited == total:
                break
            # r - 1 to l (inclusive)
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[b][i])
                visited += 1
            if visited == total:
                break
            # b - 1 to t + 1 (inclusive)
            for i in range(b - 1, t, -1):
                res.append(matrix[i][l])
                visited += 1
            if visited == total:
                break
            
            l += 1
            r -= 1
            t += 1
            b -= 1

        return res
        
