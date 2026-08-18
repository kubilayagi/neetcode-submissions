class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix = suffix = 1
        pres = sres = -11
        for i in range(0, len(nums)):
            if nums[i] == 0:
                prefix = 1
                pres = max(0, pres)
                continue
            prefix *= nums[i]
            pres = max(pres, prefix)
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] == 0:
                suffix = 1
                sres = max(0, sres)
                continue
            suffix *= nums[j]
            sres = max(sres, suffix)

        return max(pres, sres)