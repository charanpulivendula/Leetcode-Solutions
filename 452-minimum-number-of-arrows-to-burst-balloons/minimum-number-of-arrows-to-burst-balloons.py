from heapq import heappush,heappop
# class point:
#     def __init__(self,first,second):
#         self.first = first
#         self.second = second
#     def __lt__(p1,p2):
#         return p1.first<p2.first
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        # print(points)
        i = 1
        count = 1
        while(i<len(points)):
            left = max(points[i-1][0],points[i][0])
            right = min(points[i-1][1],points[i][1])
            if left<=right:
                points [i] = [left,right]
            else:
                count+=1
            i+=1

        return count      

        
        
        