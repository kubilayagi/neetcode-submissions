class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([])
        for n in nums:
            reslen = len(res)
            for i in range(0, reslen):
                res.append(res[i] + [n])

        return res