class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 1
        count = 0
        dp = [[False] * n for i in range(n)]
        dp[0][0] = True

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    # one character palindrome
                    dp[i][j] = True
                    count += 1
                elif s[i] == s[j] and j - i == 1:
                    # two character palindrome
                    dp[i][j] = True
                    count += 1
                elif s[i] == s[j] and dp[i+1][j-1]:
                    # everything else
                    dp[i][j] = True
                    count += 1

        return count