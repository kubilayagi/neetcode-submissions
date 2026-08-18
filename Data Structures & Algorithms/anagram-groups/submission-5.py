class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r = {}
        res = []
        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            rkey = tuple(counts)
            if rkey in r:
                r[rkey].append(s)
            else:
                r[rkey] = [s]

        return list(r.values())