class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(total, subres, i):
            nonlocal res
            if total > target:
                return
            elif total == target:
                res.append(subres.copy())
            
            for j in range(i, len(nums)):
                total += nums[j]
                subres.append(nums[j])
                dfs(total, subres, j)
                subres.pop()
                total -= nums[j]

            return

        dfs(0, [], 0)
        return res