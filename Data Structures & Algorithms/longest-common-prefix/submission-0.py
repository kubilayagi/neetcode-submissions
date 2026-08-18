class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlen = 201
        minstr = ""
        for s in strs:
            if len(s) < minlen:
                minlen = len(s)
                minstr = s

        i = 0
        while i < minlen:
            print(i, minlen)
            c = minstr[i]
            for s in strs:
                if s[i] != c:
                    return minstr[:i]
            i+=1

        return minstr[:i]