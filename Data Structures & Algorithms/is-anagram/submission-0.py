class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for c in s:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1
        
        for c in t:
            if c in counts:
                counts[c] -= 1
            else:
                return False
        
        for count in list(counts.values()):
            if count != 0:
                return False

        return True