class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        i = 0
        if not strs:
            return ""
        elif len(strs) == 1:
            return strs[0]
        while True:
            if i >= len(strs[0]):
                return res
            c = strs[0][i]
            for s in strs[1:]:
                if i >= len(s):
                    return res
                elif s[i] != c:
                    return res
            res += c
            i += 1

        return res