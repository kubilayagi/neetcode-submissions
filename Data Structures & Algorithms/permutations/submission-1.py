class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums, 0)
        return self.res

    def backtrack(self, nums, l):
            if l >= len(nums):
                self.res.append(nums.copy())
                return
            for r in range(l, len(nums)):
                nums[l], nums[r] = nums[r], nums[l]
                self.backtrack(nums, l + 1)
                nums[l], nums[r] = nums[r], nums[l]