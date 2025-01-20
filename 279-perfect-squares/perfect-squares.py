class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')]*(n+1)
        req = int(math.sqrt(n)//1)
        for i in range(1,req+1):
            dp[i*i]=1
        dp[0] = 1
        for i in range(1,len(dp)):
            mini = dp[i]
            for j in range(req+1):
                if i>=j*j:
                    mini = min(mini,dp[i-(j*j)])
            dp[i] = 1+mini
        print(dp)
        return dp[n]-1

        