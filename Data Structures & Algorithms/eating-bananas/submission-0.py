class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search between 0 and max(piles) until
        # you find a number (your rate) that satisfies the requirement
        # of eating all the bananas

        # maybe we can compute the sum of all the values?
        l, r = 1, max(piles)
        res = r
        while l <= r:
            k = (r+l) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
