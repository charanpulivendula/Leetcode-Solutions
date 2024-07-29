from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dep = [[] for _ in range(numCourses)]
        sources = [True for _ in range(numCourses)]
        res = []
        for a,b in prerequisites:
            dep[a].append(b)
            sources[b] = False
        
        visited = set()
        def dfs(node,stack):
            stack.append(node)
            visited.add(node)
            for neigbour in dep[node]:
                if neigbour in visited:
                    if neigbour in stack:
                        return False
                else:
                    dfs(neigbour,stack)
            stack.remove(node)
            res.append(node)
            return True

        for source in range(len(sources)):
            if sources[source]:
                if not dfs(source,[]):
                    return []
        if len(res) == numCourses:
            return res
        else:
            return []
        


