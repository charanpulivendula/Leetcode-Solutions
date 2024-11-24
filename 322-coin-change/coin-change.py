class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [float("inf") for _ in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            if coin<=amount:
                dp[coin] = 1
        for i in range(1,len(dp)):
            for coin in coins:
                if i - coin >= 0 :
                    dp[i] = min(dp[i],1+dp[i-coin])

        if dp[len(dp)-1] == 0 or dp[len(dp)-1] == float("inf"):
            return -1
        else:
            return dp[len(dp)-1]
        