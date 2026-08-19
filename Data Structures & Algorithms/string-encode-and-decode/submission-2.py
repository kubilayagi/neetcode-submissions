class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc += str(len(s)) + "#" + s
        return enc


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            count = ""
            while s[i] != "#":
                count = count + s[i]
                i += 1
            i += 1
            res.append(s[i:(i+int(count))])
            i += int(count)

        return res
