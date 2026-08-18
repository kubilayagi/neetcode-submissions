class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        mid = l + ((r - l) // 2)
        while l < r:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid
            mid = l + ((r - l) // 2)
        return mid