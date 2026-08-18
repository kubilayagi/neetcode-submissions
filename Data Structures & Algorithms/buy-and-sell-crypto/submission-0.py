class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        res = 0
        while r < len(prices):
            if prices[r] <= prices[l]:
                l = r
            elif prices[r] > prices[l]:
                res = max(res, prices[r] - prices[l])
            r += 1
        return res