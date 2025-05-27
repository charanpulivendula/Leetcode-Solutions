from queue import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        distances = [[float('inf')]*n for _ in range(m)]
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        q = deque([])
        def isvalid(i,j):
            return 0<=i<m and 0<=j<n

        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    distances[i][j] = 0
                    q.append((i,j,0))
        while(q):
            nodeX,nodeY,dist = q.popleft()
            for direction in directions:
                newX = nodeX+direction[0]
                newY = nodeY+direction[1]
                if isvalid(newX,newY):
                    if 1+dist<distances[newX][newY]:
                        distances[newX][newY] = 1+dist
                        q.append((newX,newY,1+dist))
        return distances


