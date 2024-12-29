class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        adj = [set() for _ in range(n)]
        visited = set()
        outdegrees = [0 for _ in range(n)]
        res = []
        queue = deque()
        for req in prerequisites:
            adj[req[0]].add(req[1])
            outdegrees[req[0]]+=1
        for index,deg in enumerate(outdegrees):
            if deg==0:
                queue.append(index)
                visited.add(index)
        print(outdegrees)
        while(queue):
            node= queue.popleft()
            for index in range(len(adj)):
                if index not in visited and node in adj[index]:
                    outdegrees[index]-=1
                    if outdegrees[index]==0:
                        queue.append(index)
                        visited.add(index)
        print(outdegrees)
        
        return sum(outdegrees) == 0

        
        # def bfs(node):
        #     queue = deque()

        
        # for i in range(len(sources)):
        #     if sources[i]:
        #         if not bfs(i,[]):
        #             return False
        
        # return len(res) == numCourses
 