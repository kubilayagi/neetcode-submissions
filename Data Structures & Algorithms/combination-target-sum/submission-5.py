class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, total, cur):
            nonlocal res
            if total > target:
                return
            for j in range(i, len(nums)):
                cur.append(nums[j])
                total += nums[j]
                if total == target:
                    res.append(cur.copy())
                    total -= nums[j]
                    cur.pop()
                    continue
                backtrack(j, total, cur)
                cur.pop()
                total -= nums[j]

        backtrack(0, 0, [])
        return res