class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[float("inf") for _ in range(n)] for _ in range(n)]
        dp[0][0] = triangle[0][0]
        for i in range(1,n):
            dp[i][0] = triangle[i][0]+dp[i-1][0]
            dp[i][i] = triangle[i][i]+dp[i-1][i-1]
            
        for i in range(1,n):
            for j in range(1,i):
                dp[i][j] = triangle[i][j]+min(dp[i-1][j-1],dp[i-1][j])
        
        return min(dp[n-1])
                