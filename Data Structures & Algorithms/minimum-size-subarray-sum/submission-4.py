class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = float('inf')
        curSum = 0
        curLen = 0
        for r in range(len(nums)):
            curSum += nums[r]
            curLen += 1
            while curSum >= target:
                res = min(res, curLen)
                curSum -= nums[l]
                curLen -= 1
                l += 1
        return res if res != float('inf') else 0

        