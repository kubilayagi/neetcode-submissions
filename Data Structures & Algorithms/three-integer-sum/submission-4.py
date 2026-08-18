class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        k = 2

        while k < len(nums):
            if nums[k] < 0:
                k+=1
                continue
            i, j = 0, k-1
            while i < j:
                total = nums[i] + nums[j] + nums[k]
                tup = (nums[i], nums[j], nums[k])
                if total == 0:
                    res.add(tup)
                    i+=1
                    j-=1
                elif total < 0:
                    i+=1
                elif total > 0:
                    j-=1
            k+=1

        return [list(t) for t in res]