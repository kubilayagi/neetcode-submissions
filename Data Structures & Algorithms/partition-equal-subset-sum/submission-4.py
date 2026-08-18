class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        h = s // 2
        if s % 2 == 1 or not nums or len(nums) == 1:
            return False
        
        dp = [[False] * (h + 1) for _ in range(len(nums) + 1)]
        for t in range(len(nums) + 1): # stupid question requirements
            dp[t][0] = True 
        
        for i in range(1, len(nums) + 1):
            for j in range(1, h + 1):
                if j - nums[i-1] >= 0:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
            
        return dp[len(nums)][h]