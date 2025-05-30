from heapq import heappush,heappop
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        heap = []
        indegree = defaultdict(set)
        for a,b in prerequisites:
            indegree[b].add(a)
        print(indegree)
        for node in range(numCourses):
            if node not in indegree:
                heappush(heap,node)

        visited = set()
        while(heap):
            node = heappop(heap)
            res = [node]+res
            visited.add(node)
            for neighbor in indegree:
                if neighbor not in visited and node in indegree[neighbor]:
                    indegree[neighbor].remove(node)
                    if not indegree[neighbor]:
                        heappush(heap,neighbor)

        if len(res)==numCourses:
            return res
        else:
            return []




        
        


