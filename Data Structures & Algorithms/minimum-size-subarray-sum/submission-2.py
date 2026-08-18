class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        curSum = 0
        minLen = float('inf')
        curLen = 0
        while r < len(nums):
            curSum += nums[r]
            curLen += 1
            while curSum >= target:
                if curLen < minLen:
                    minLen = curLen
                curSum -= nums[l]
                l += 1
                curLen -= 1
            r += 1

        return minLen if minLen != float('inf') else 0