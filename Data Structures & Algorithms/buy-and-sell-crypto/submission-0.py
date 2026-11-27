class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minP, maxP = prices[0], prices[0]
        res = 0
        for i in range(len(prices)):
            if prices[i] < minP:
                minP = prices[i]
                maxP = prices[i]
            if prices[i] > maxP:
                maxP = prices[i]
            res = max(res, maxP - minP)
        return res