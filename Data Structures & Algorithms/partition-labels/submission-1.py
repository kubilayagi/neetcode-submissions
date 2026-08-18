class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if len(s) < 1:
            return []
        elif len(s) == 1:
            return [1]
        lastseen = {}
        res = []
        for i, c in enumerate(s):
            lastseen[c] = i

        maxlast = lastseen[s[0]]
        l = 0
        for i, c in enumerate(s):
            maxlast = max(maxlast, lastseen[c])
            if i == maxlast:
                res.append(i - l + 1)
                l = i + 1
                

        print(res)
        return res