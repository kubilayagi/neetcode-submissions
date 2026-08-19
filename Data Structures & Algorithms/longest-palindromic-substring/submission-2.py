class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxlen = 0
        for i in range(len(s)):
            l = r = i
            count = 0
            cur = ""
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count = r - l + 1
                cur = s[l:r+1]
                l -= 1
                r += 1
            if count > maxlen:
                maxlen = count
                res = cur

            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count = r - l + 1
                cur = s[l:r+1]
                l -= 1
                r += 1
            if count > maxlen:
                maxlen = count
                res = cur
        return res