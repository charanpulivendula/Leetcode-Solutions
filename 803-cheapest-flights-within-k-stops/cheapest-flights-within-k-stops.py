from queue import deque
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        distances = [float('inf') for _ in range(n)]
        distances[src] = 0
        q = deque([])
        q.append((0,src))
        for s, d ,dist in flights:
            graph[s].append((dist,d))
        stops = 0

        while(q and stops<=k):
            length = len(q)
            for _ in range(length):
                curr,city = q.popleft()
            
                for dist,neighbor in graph[city]:
                    if curr+dist<distances[neighbor]:
                        distances[neighbor] = curr+dist
                        q.append((curr+dist,neighbor))
            stops+=1
        return distances[dst] if distances[dst]!=float('inf') else -1
