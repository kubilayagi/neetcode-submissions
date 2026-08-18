class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return
            if total > target:
                return
            if i >= len(nums):
                return
            subset.append(nums[i])
            total += nums[i]
            # print(total, subset)
            dfs(i, total)
            popped = subset.pop()
            total -= popped
            dfs(i+1, total)
        
        dfs(0, 0)
        return res