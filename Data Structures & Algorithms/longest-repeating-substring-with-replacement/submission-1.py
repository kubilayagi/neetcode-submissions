class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        l = 0
        res = k
        maxfreq = 0
        for r in range (0, len(s)):
            counts[s[r]] = 1 + counts.get(s[r], 0)
            maxfreq = max(maxfreq, counts[s[r]])

            while maxfreq + k < r - l + 1:
                counts[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
            
        return res