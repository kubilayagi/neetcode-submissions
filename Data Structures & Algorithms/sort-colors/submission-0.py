class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3
        for n in nums:
            counts[n] += 1
        
        r = []
        for i, c in enumerate(counts):
            for j in range(c):
                r.append(i)

        for i, v in enumerate(r):
            nums[i] = v
