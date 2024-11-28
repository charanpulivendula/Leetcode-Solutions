class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = abs(obstacleGrid[0][0]-1)
        for i in range(1,m):
            if not obstacleGrid[i][0]:
                dp[i][0] = dp[i-1][0]
        for j in range(1,n):
            if not obstacleGrid[0][j]:
                dp[0][j] = dp[0][j-1]
        
        for i in range(1,m):
            for j in range(1,n):
                if not obstacleGrid[i][j]:
                    if not obstacleGrid[i-1][j]:
                        dp[i][j] += dp[i-1][j]
                    if not obstacleGrid[i][j-1]:
                        dp[i][j] += dp[i][j-1]
        return dp[m-1][n-1]




        