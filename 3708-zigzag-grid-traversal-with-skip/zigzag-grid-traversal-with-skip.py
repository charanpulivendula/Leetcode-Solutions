class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        count = 0
        m = len(grid)
        n = len(grid[0])
        res = []
        row  = 0
        while(row < m):
            for i in range(0,n,2):
                res.append(grid[row][i])
            row+=1
            if row>=m:
                return res
            if n%2==0:
                itr = n-1
            else:
                itr = n-2
            for i in range(itr,-1,-2):
                res.append(grid[row][i])
            row+=1
        return res

        