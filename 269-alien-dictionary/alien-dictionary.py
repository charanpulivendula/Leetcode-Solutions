from collections import defaultdict
# from sortedcollections import OrderedSet
from queue import deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        q = deque([])
        res = ""
        indegree = {c: 0 for word in words for c in word}
        graph = defaultdict(list)
        for i in range(len(words)-1):
            first = words[i]
            second = words[i+1]
            if len(first) > len(second) and first.startswith(second):
                return ""
            for j in range(min(len(first),len(second))):
                if first[j]!=second[j]:
                    if second[j] not in graph[first[j]]:
                        graph[first[j]].append(second[j])
                        indegree[second[j]]+=1
                    break
        
        for node in indegree:
            if indegree[node]==0:
                q.append(node)
        print(graph)

        while q:
            node = q.popleft()
            res+=node
            for neighbor in graph[node]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    q.append(neighbor)
        
        if len(res)!=len(graph):
            return ""
        return res


                
