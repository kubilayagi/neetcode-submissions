class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins and amount > 0:
            return -1
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            mincoins = float('inf')
            for c in coins:
                if c > i:
                    continue
                if dp[i - c] != float('inf'): # ie there was no way to solve that subproblem
                    dp[i] = min(dp[i], 1 + dp[i - c])

        return -1 if dp[amount] == float('inf') else dp[amount]