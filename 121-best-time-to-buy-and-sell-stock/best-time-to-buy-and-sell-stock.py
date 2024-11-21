class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftmin = prices[0]
        profit = 0
        for price in prices:
            if price < leftmin:
                leftmin = price
            profit = max(profit,price-leftmin)
        return profit