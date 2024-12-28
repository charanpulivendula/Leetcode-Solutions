from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)
        for i, equation in enumerate(equations):
            adjList[equation[0]].append((equation[1],values[i]))
            adjList[equation[1]].append((equation[0],1/values[i]))
        res = []

        def dfs(source,destination,visited,res):
            if source == destination:
                return res
            visited.add(source)

            for neighbor in adjList[source]:
                if neighbor[0] not in visited:
                    ans = dfs(neighbor[0],destination,visited,res*neighbor[1])
                    if ans!=-1.00000:
                        return ans
            return -1.00000

        for query in queries:
            if query[0] not in adjList or query[1] not in adjList:
                res.append(-1.00000)
            else:
                visited = set() 
                res.append(dfs(query[0],query[1],visited,1))
        
        return res



        