class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        m = 0
        while l <= r:
            m = int((r-l)/2) + l
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        pivot = m

        l, r = 0, len(nums)-1
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot

        while l <= r:
            m = int((r-l)/2) + l
            if target < nums[m]:
                r = m-1
            elif target > nums[m]:
                l = m+1
            else:
                return m
        return -1
        


