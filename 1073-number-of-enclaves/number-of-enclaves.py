class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited=set()

        def isvalid(i,j):
            return 0<=i<m and 0<=j<n and grid[i][j]==1 and (i,j) not in visited

        def dfs(i,j):
            if not isvalid(i,j):
                return
            visited.add((i,j))
            grid[i][j] = 0
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i-1,j)

        for i in range(m):
            for j in range(n):
                if i==0 or j == 0 or i == m-1 or j == n-1:
                    if grid[i][j] == 1:
                        dfs(i,j)
        counter = 0
        print(grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    counter+=1
        return counter