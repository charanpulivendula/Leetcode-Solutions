class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        neighbors = [[] for _ in range(n)]
        visited = [False for _ in range(n)]
        sources = [True for _ in range(n)]
        res = []

        for req in prerequisites:
            neighbors[req[0]].append(req[1])
            sources[req[1]]= False
        
        def dfs(node,stack):
            if visited[node]:
                return False
            stack.append(node)
            visited[node] = True
            for neighbor in neighbors[node]:
                if visited[neighbor]:
                    if neighbor in stack:
                        return False
                dfs(neighbor,stack)
            stack.remove(node)
            res.append(node)
            return True
        
        for i in range(len(sources)):
            if sources[i]:
                if not dfs(i,[]):
                    return False
        
        return len(res) == numCourses
 