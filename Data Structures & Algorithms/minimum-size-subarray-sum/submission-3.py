class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        curSum = 0
        minLen = float('inf')
        curLen = 0
        while r < len(nums):
            curSum += nums[r]
            curLen += 1
            # key thing to note here is that we do this while loop because we
            # always want to check if there is a way to decrease our size
            # with the current window. because the new number we just added
            # to the list might be quite big, so we might be able to remove
            # a few earlier ones from the left side of the window
            while curSum >= target:
                if curLen < minLen:
                    minLen = curLen
                curSum -= nums[l]
                l += 1
                curLen -= 1
            r += 1

        return minLen if minLen != float('inf') else 0

'''
I think some intuition built here is that we want to use sliding window
when the answer is looking for an answer based on one contiguous subarray/substring

we use backtracking when we are picking and choosing random elements from an array/string

we combine the two when we are looking to build different combinations of contiguous
subarrays/substrings
'''