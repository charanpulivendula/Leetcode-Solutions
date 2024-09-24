
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        directions = [(1,0),(0,1),(0,-1),(-1,0)]
        def valid(i,j):
            return 0<=i<m and 0<=j<n and grid[i][j] == 1
        
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j,0))

        visited = set()

        maxtime = 0
        while q:
            i,j,time = q.popleft()
            visited.add((i,j))
            maxtime = max(maxtime,time)
            for x,y in directions:
                if valid(i+x,j+y) and (i+x,j+y) not in visited:
                    grid[i+x][j+y] = 2
                    q.append((i+x,j+y,time+1))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return maxtime




        

