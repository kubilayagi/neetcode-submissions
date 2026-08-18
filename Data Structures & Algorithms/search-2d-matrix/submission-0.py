class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first to column-wise b search, then row wise

        t, b = 0, len(matrix)-1

        row = -1

        while t <= b:
            m = int((b-t)/2 + t)
            if target < matrix[m][0]:
                b = m-1
            elif target > matrix[m][-1]:
                t = m+1
            else:
                row = m
                break
        print('row', row)
        l, r = 0, len(matrix[row])-1

        while l <= r:
            m = int((r-l)/2 + l)
            if target < matrix[row][m]:
                r = m-1
            elif target > matrix[row][m]:
                l = m+1
            else:
                return True
        return False
        