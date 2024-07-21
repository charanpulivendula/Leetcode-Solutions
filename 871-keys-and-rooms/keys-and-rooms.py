class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False for i in range(len(rooms))]
        def dfs(room):
            if visited[room]:
                return
            visited[room] = True
            for key in rooms[room]:
                dfs(key)
        dfs(0)
        for state in visited:
            if not state:
                return False
        return True