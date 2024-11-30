class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        maxsq = int(dp[0][0])
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            maxsq = max(maxsq,dp[i][0])
        
        for j in range(1,n):
            dp[0][j] = int(matrix[0][j])
            maxsq = max(maxsq,dp[0][j])

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]=="1":
                    dp[i][j] = 1 + min(int(dp[i-1][j]),int(dp[i-1][j-1]),int(dp[i][j-1]))
                    maxsq = max(maxsq,dp[i][j])

        return maxsq**2
        
        

        