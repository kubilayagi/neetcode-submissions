class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        holdingStock = False
        boughtPrice = 10001
        profit = 0
        n = len(prices)
        i = 0

        while i < n:
            if holdingStock:
                if (i+1) >= n:
                    profit += prices[i] - boughtPrice
                    return profit
                elif prices[i+1] < prices[i]:
                    profit += prices[i] - boughtPrice
                    holdingStock = False
                    boughtPrice = 10001
                    i += 1
                elif prices[i+1] >= prices[i]:
                    i += 1
                    continue
            if not holdingStock:
                while i < n - 1 and prices[i+1] < prices[i]:
                    i += 1

                holdingStock = True
                boughtPrice = prices[i]

        return profit