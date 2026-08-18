class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        maxseqlen = 1

        while s:
            n = s.pop()
            seqlen = 1
            rn, ln = n+1, n-1
            while rn in s:
                s.remove(rn)
                rn += 1
                seqlen += 1
            while ln in s:
                s.remove(ln)
                ln -= 1
                seqlen += 1

            maxseqlen = max(maxseqlen, seqlen)

        return maxseqlen
