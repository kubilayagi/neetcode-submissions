class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findPivot():
            nonlocal nums
            l, r = 0, len(nums) - 1
            m = -1
            while l < r:
                m = l + ((r-l)//2)
                if nums[m] > nums[r]:
                    l = m + 1
                else:
                    r = m
            return l

        def bSearch(l, r):
            nonlocal nums
            while l <= r:
                m = l + ((r-l)//2)
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1

        pivot = findPivot()
        if target > nums[-1]:
            return bSearch(0, pivot)
        else:
            return bSearch(pivot, len(nums)-1)