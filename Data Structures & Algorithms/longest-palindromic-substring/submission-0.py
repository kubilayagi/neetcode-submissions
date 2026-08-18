class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxI = 0
        maxJ = 0
        dp = [[False] * n for i in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if maxJ - maxI < j - i:
                        maxJ = j
                        maxI = i

        return s[maxI:maxJ+1]