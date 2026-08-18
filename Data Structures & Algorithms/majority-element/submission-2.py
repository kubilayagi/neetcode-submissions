class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        elif len(nums) == 1:
            return nums[0]

        res = nums[0]
        count = 1
        n = len(nums)

        for i in range(1, n):
            if nums[i] == res:
                count += 1
            else:
                count -= 1

            if count == 0:
                res = nums[i]
                count = 1

        return res