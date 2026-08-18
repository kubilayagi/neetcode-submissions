class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def solve(idx, xor):
            nonlocal res
            if idx >= len(nums):
                res += xor
                return
            cur = nums[idx]
            
            nextxor = xor ^ cur
            solve(idx+1, nextxor)
            solve(idx+1, xor)
            return
        
        solve(0, 0)
        return res