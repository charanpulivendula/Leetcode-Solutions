class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        rightprofit = [0 for _ in range(n+1)]
        leftprofit = [0 for _ in range(n)]
        l_min = prices[0]
        r_max  = prices[n-1]
        for i in range(1,n):
            if prices[i]<l_min:
                l_min = prices[i]
                leftprofit[i] = leftprofit[i-1]
            else:
                leftprofit[i] = max(leftprofit[i-1],prices[i]-l_min)
        
        for i in range(n-2,0,-1):
            if prices[i]>r_max:
                r_max = prices[i]
                rightprofit[i] = rightprofit[i+1]
            else:
                rightprofit[i] = max(rightprofit[i+1],r_max-prices[i])
        print(leftprofit,rightprofit)
        maxprofit = 0
        for i in range(n):
            maxprofit = max(maxprofit,leftprofit[i]+rightprofit[i+1])
        return maxprofit
        
            
        
        