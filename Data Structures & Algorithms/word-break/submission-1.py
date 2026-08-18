class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                wlen = len(w)
                if (i + wlen - 1) < len(s) and s[i : i + wlen] == w and not dp[i]:
                    dp[i] = dp[i + wlen]

        return dp[0]