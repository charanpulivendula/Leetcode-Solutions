from heapq import heappush,heappop
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        heap = []
        minheights = [[float('inf')]*n for _ in range(m)]
        minheights[0][0] = 0
        heappush(heap,(0,0,0))
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        def isValid(i,j):
            return 0<=i<m and 0<=j<n

        while heap:
            curr,x,y = heappop(heap)
            if x == m-1 and y == n-1:
                return curr
            for dx,dy in directions:
                newX = x+dx
                newY = y+dy
                if isValid(newX,newY):
                    diff = abs(heights[newX][newY]-heights[x][y])
                    currmax = max(curr,diff)
                    if currmax<minheights[newX][newY]:
                        minheights[newX][newY] = currmax
                        heappush(heap,(currmax,newX,newY))