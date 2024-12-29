class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        queue = deque()
        visited = dict()
        for start in range(len(graph)):
            if start not in visited:
                queue.append(start)
                visited[start] = 1
                while(queue):
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            queue.append(neighbor)
                            visited[neighbor] = -1*visited[node]
                        else:
                            if visited[neighbor] == visited[node]:
                                return False
        return True



