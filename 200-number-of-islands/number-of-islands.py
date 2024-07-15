class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1),(-1,0),(1,0),(0,-1)]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        def checker(grid,i ,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                return False
            return True
        def dfs(grid,visited,x,y):
            if not checker(grid,x,y):
                return
            for (i,j) in directions:
                if checker(grid,x+i,y+j) and grid[x+i][y+j]=='1' and not visited[x+i][y+j]:
                    visited[x+i][y+j] = True
                    dfs(grid,visited,x+i,y+j)
                
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and visited[i][j] == False:
                    count+=1
                    visited[i][j] = True
                    dfs(grid,visited,i,j)
        print(visited)
        return count
        
