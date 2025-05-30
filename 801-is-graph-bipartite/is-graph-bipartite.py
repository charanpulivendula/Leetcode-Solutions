from collections import defaultdict
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        visited = defaultdict(int)

        def dfs(node):

            for neighbor in graph[node]:
                if neighbor in visited:
                    if visited[neighbor]==visited[node]:
                        return False
                    
                else:
                    visited[neighbor] = -1*visited[node]
                    if not dfs(neighbor):
                        return False

            return True
        for node in range(len(graph)):
            if node not in visited:
                visited[node] = 1
                if not dfs(node):
                    return False
        return True



