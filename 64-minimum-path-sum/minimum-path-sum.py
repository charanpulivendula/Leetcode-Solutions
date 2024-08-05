class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        def checker(i,j):
            return 0<=i<len(grid) and 0<=j<len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if checker(i-1,j):
                    dp[i][j] = min(dp[i][j],dp[i-1][j]+grid[i][j])
                if checker(i,j-1):
                    dp[i][j] = min(dp[i][j],dp[i][j-1]+grid[i][j])

        return dp[-1][-1]
        
        

        