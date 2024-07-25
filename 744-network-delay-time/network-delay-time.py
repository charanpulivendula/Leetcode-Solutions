class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist_tracker = [float("inf")]*(n+1)
        dist_tracker[k] = 0
        adj_List = [[] for _ in range(n+1)]
        for a,b,w in times:
            adj_List[a].append((b,w))
        def dfs(node,val):
            print(node,val)
            if val>dist_tracker[node]:
                return
            dist_tracker[node] = val
            for neigbour,traveltime in adj_List[node]:
                if traveltime+val < dist_tracker[neigbour]:
                    dfs(neigbour,traveltime+val)

        dfs(k,0)
        maxi = -1
        for i in range(1,len(dist_tracker)):
            maxi = max(maxi,dist_tracker[i])
        if maxi == float("inf"):
            return -1
        return maxi


        