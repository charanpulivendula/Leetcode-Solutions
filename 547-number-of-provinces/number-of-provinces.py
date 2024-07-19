class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = [[0 for i in range(len(isConnected))] for j in range(len(isConnected))]
        def dfs(i):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and not visited[i][j]:
                    visited[i][j] = 1
                    dfs(j)
            return
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and not visited[i][j]:
                    provinces += 1
                    visited[i][j] = 1
                    dfs(j)
        return provinces
