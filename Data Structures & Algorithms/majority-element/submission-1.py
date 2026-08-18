class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.altSolution(nums)
        # counts = Counter(nums)
        # for k, v in counts.items():
        #     if v > len(nums) // 2:
        #         return k
        # return -1

    def altSolution(self, nums: List[int]) -> int:
        res, count = None, 0

        for n in nums:
            if count == 0:
                res = n
            count += 1 if n == res else -1

        return res
