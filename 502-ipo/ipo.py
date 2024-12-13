from heapq import heappush,heappop
class Solution:

    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        points = list(zip(capital,profits))
        points.sort()
        heap = []
        n = len(profits)
        i = 0
        ptr = 0
        while(i<k):
            while(ptr<n and w>=points[ptr][0]):
                heappush(heap,-points[ptr][1])
                ptr+=1
            if not heap:
                break
            w+=-heappop(heap)
            i+=1
        return w
            
            


        