class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMinPrice = 101
        currMaxProfit = 0
        for price in prices:
            currMinPrice = min(currMinPrice, price)
            currMaxProfit = max(currMaxProfit, price - currMinPrice)
        return currMaxProfit