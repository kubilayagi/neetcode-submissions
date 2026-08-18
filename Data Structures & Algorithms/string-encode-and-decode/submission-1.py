class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            lenstr = ""
            while s[i] != "#":
                lenstr += str(s[i])
                i += 1
            i += 1
            lennum = int(lenstr)
            curstr = ""
            for j in range(i, lennum + i):
                curstr += str(s[i])
                i += 1
            res.append(curstr)
        return res
