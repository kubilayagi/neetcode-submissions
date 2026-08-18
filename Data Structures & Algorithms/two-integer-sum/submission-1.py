class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for i, n in enumerate(nums):
            if n in s:
                return [s[n], i]
            else:
                s[target - n] = i

        return None