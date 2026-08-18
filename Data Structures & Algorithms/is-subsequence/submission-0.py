class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = tp = 0
        while tp < len(t):
            print(sp, tp)
            if sp == len(s):
                return True
            if s[sp] == t[tp]:
                sp += 1
            tp += 1

        return sp == len(s)