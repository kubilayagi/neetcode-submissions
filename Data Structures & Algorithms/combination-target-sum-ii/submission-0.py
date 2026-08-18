class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        print(candidates)

        res = []
        subset = []

        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return
            if total > target:
                return
            if i >= len(candidates):
                return
            subset.append(candidates[i])
            total += candidates[i]
            # print(total, subset)
            dfs(i+1, total)
            popped = subset.pop()
            total -= popped
            while i < len(candidates) - 1:
                if candidates[i] == candidates[i+1]:
                    i += 1
                else:
                    break
            dfs(i+1, total)
        
        dfs(0, 0)
        return res