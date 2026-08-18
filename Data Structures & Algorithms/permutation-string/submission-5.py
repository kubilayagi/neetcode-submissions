class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1counts, s2counts = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1counts[ord(s1[i]) - ord('a')] += 1
            s2counts[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1counts[i] == s2counts[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            rindex = ord(s2[r]) - ord('a')
            s2counts[rindex] += 1
            if s2counts[rindex] == s1counts[rindex]:
                matches += 1
            elif s2counts[rindex] == s1counts[rindex] + 1:
                matches -= 1
            
            lindex = ord(s2[l]) - ord('a')
            s2counts[lindex] -= 1
            if s2counts[lindex] == s1counts[lindex]:
                matches += 1
            elif s2counts[lindex] == s1counts[lindex] - 1:
                matches -= 1
            l += 1

        return matches == 26


