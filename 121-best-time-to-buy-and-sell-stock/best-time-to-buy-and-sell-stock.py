class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minLeft = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if minLeft < prices[i]:
                profit = max(profit,prices[i]-minLeft)
            else:
                minLeft = prices[i]
        return profit
        
        