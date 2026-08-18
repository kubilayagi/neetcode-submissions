class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        res = 0
        if len(s) < 2:
            return len(s)
        l, r = 0, 0
        while r < len(s):
            if s[r] in chars:
                l = max(chars[s[r]] + 1, l)
            chars[s[r]] = r
            res = max(res, r - l + 1)
            r += 1
        return res