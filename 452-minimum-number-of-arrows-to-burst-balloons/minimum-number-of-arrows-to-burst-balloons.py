from heapq import heappush,heappop

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        heap = []
        for point in points:
            heappush(heap,point)
        count = 0
        while(len(heap)>1):
            first = heappop(heap)
            second = heappop(heap)
            left = max(first[0],second[0])
            right = min(first[1],second[1])
            if left <= right:
                heappush(heap,[left,right])
            else:
                count+=1
                heappush(heap,second)
        return count+1
        
        