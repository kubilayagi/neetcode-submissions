class Solution:
    def numSquares(self, n: int) -> int:
        dp = [10001] * n
        dp[0] = 1

        for i in range(1, n+1):
            squares = [(j**2) for j in range(1, int(math.sqrt(i)) + 1)]
            print(i, squares)
            for s in squares:
                if s == i:
                    dp[i - 1] = 1
                else:
                    dp[i - 1] = min(dp[i - 1], 1 + dp[i-s-1])

        return dp[n-1]