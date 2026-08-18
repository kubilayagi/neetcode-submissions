class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix)
        m = -1
        while t < b:
            m = t + ((b-t) // 2)
            if matrix[m][0] <= target and matrix[m][-1] >= target:
                break
            elif matrix[m][0] > target:
                b = m
            elif matrix[m][-1] < target:
                t = m + 1

        if matrix[m][0] == target or matrix[m][-1] == target:
            return True

        nums = matrix[m]
        l, r = 0, len(nums)
        while l < r:
            m = l + ((r-l) // 2)
            if target == nums[m]:
                return True
            elif target < nums[m]:
                r = m
            else:
                l = m + 1

        return False