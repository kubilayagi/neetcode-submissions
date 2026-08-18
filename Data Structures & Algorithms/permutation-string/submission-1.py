class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1count, s2count = [0] * 26, [0] * 26

        for i in range(0, len(s1)):
            s1count[ord(s1[i]) - ord('a')] += 1
            s2count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1count[i] == s2count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # check right value
            rchar = ord(s2[r]) - ord('a')
            s2count[rchar] += 1
            if s1count[rchar] == s2count[rchar]:
                matches += 1
            elif s1count[rchar] == s2count[rchar] - 1: #i.e. we messed up a match that already existed
                matches -= 1

            # check left value (opposite of right char basically since we're removing it from our window)
            lchar = ord(s2[l]) - ord('a')
            s2count[lchar] -= 1
            if s1count[lchar] == s2count[lchar]:
                matches += 1
            elif s1count[lchar] == s2count[lchar] + 1: #i.e. we messed up a match that already existed
                matches -= 1
                        
            l += 1

        return matches == 26