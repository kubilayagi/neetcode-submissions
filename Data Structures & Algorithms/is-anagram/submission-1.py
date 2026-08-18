class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        scount, tcount = [0] * 26, [0] * 26
        if len(s) != len(t):
            return False
        for c in s:
            scount[ord(c) - ord('a')] += 1
        for c in t:
            tcount[ord(c) - ord('a')] += 1
        return scount == tcount