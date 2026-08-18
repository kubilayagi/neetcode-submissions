class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ''
        for s in strs:
            enc = enc + str(len(s)) + '#' + s
        return enc

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            numstr = ''
            while s[i] != '#':
                numstr = numstr + s[i]
                i+=1
            i+=1
            num = int(numstr)
            decstr = ''
            j = i
            while i < j + num:
                decstr = decstr + s[i]
                i+=1
            print(decstr)
            res.append(decstr)
        return res