class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
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
                dfs(total, subres, j) # start from j here because we can reuse the same number
                subres.pop()
                total -= nums[j]

            return

        dfs(0, [], 0)
        return res