class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        k%=len(nums)
        i = 0
        while i < k:
            n = nums.pop()
            nums.insert(0, n)
            i+=1

        return