class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res

    def altSolutionSubsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        res.append([])
        for n in nums:
            reslen = len(res)
            for i in range(0, reslen):
                res.append(res[i] + [n])

        return res