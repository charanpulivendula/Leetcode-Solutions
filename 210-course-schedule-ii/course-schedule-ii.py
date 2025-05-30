from heapq import heappush,heappop
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        heap = []
        indegree = [0]*numCourses
        graph = defaultdict(list)
        for a,b in prerequisites:
            indegree[b]+=1
            graph[a].append(b)
        
        for node in range(numCourses):
            if indegree[node]==0:
                heappush(heap, node)

        visited = set()
        while(heap):
            node = heappop(heap)
            res = [node]+res
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    indegree[neighbor]-=1
                    if indegree[neighbor]==0:
                        heappush(heap,neighbor)

        if len(res)==numCourses:
            return res
        else:
            return []




        
        


