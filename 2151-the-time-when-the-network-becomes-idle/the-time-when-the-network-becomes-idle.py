from collections import deque,defaultdict

class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        dist = [float('inf') for _ in range(len(patience))]
        visited = [False for _ in range(len(patience))]
        dist[0] = 0
        q = deque()
        q.append((0,0))
        adj = defaultdict(list)

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)


        # time_taken = min(2*distance,response) + (2*distance/response)
        def bfs():

            while(q):
                node,cur_dist = q.popleft()
                visited[node] = True
                for neighbour in adj[node]:
                    if not visited[neighbour] and cur_dist+1<dist[neighbour]:
                        dist[neighbour] = cur_dist + 1
                        q.append((neighbour,cur_dist+1))
        
        bfs()
        dist = list(map(lambda x: x*2,dist))
        time_taken = 0
        print(dist)
        for i in range(1,len(patience)):
            mod = dist[i]%patience[i]
            if patience[i]>dist[i]:
                time = dist[i]
            elif mod == 0:
                time = dist[i] + (dist[i] - patience[i])
            else:
                time = dist[i]+(dist[i]-mod) 

            time_taken = max(time,time_taken)
        
        return time_taken+1

                
            
