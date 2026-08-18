class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use a set to keep track of the unique characters
        if len(s) == 0 or len(s) == 1:
            return len(s)
        l, r = 0, 0
        res = 0
        chars = set()
        while r < len(s):
            if s[r] in chars:
                while s[r] in chars:
                    chars.remove(s[l])
                    l += 1
            chars.add(s[r])
            res = max(res, r - l + 1)
            r += 1
        return res