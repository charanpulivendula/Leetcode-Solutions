class Solution:
  def networkDelayTime(self, times, n, k):
    adj = [[] for _ in range(n+1)]
    distance = [float("inf")]*(n+1)
    for s,d,w in times:
      adj[s].append((d,w))
      
    def dfs(node,val):
      if val >= distance[node]:
        return
      distance[node] = val
      for neighbour,traveltime in adj[node]:
        if val+traveltime < distance[neighbour]:
          dfs(neighbour,val+traveltime)
    
    dfs(k,0)
    print(distance)
    for i in range(1,n+1):
      if distance[i] == float('inf'):
        return -1

    return max(distance[1:])