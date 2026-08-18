class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        # it costs nothing to stay on the ground, and nothing to step onto the first staircase
        dp[0] = 0
        dp[1] = 0
        for i in range(2, len(cost) + 1):
            dp[i] = min(cost[i-1] + dp[i-1], cost[i-2] + dp[i-2])

        return dp[len(cost)]