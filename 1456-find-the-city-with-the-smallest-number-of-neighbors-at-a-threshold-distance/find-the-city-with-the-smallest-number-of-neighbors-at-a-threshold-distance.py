from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        
        # Build adjacency list
        for u, v, wt in edges:
            graph[u].append((v, wt))
            graph[v].append((u, wt))
        
        def dijkstra(src):
            heap = []
            dist = [float('inf')] * n
            dist[src] = 0
            heappush(heap, (0, src))
            
            while heap:
                curr_dist, u = heappop(heap)
                
                if curr_dist > dist[u]:
                    continue
                
                for v, wt in graph[u]:
                    if dist[u] + wt < dist[v]:
                        dist[v] = dist[u] + wt
                        heappush(heap, (dist[v], v))
            
            # Count how many cities are reachable (excluding itself)
            count = sum(1 for i in range(n) if i != src and dist[i] <= distanceThreshold)
            return count
        
        res_city = -1
        min_reachable = float('inf')
        
        # Run Dijkstra from every city
        for city in range(n):
            reachable = dijkstra(city)
            
            # If tie, choose city with larger index
            if reachable <= min_reachable:
                min_reachable = reachable
                res_city = city
        
        return res_city


