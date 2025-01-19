
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        m = len(rooms)
        n = len(rooms[0])
        def isValid(i,j):
            return 0<=i<m and 0<=j<n and rooms[i][j]!=-1
        queue = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i,j))

        visited = set()
        while(queue):
            for i in range(len(queue)):
                current = queue.popleft()
                visited.add((current[0],current[1]))
                for direction in directions:
                    row = current[0]+direction[0]
                    col = current[1]+direction[1]
                    if isValid(row,col) and (row,col) not in visited:
                        queue.append((row,col))
                        rooms[row][col] = min(rooms[row][col],rooms[current[0]][current[1]]+1)
            
        return rooms







        