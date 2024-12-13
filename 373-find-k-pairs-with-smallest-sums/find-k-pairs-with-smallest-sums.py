
from heapq import heappush,heappop
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        heap = []
        heappush(heap,(nums1[0]+nums2[0],[nums1[0],nums2[0]],(0,0)))
        i = 0
        j = 0
        visited = set()
        visited.add((0,0))
        while(k>0):
            temp = heappop(heap)
            value = temp[0]
            (i,j) = temp[2]
            res.append(temp[1])
            if i<len(nums1)-1 and (i+1,j) not in visited:
                heappush(heap,(nums1[i+1]+nums2[j],[nums1[i+1],nums2[j]],(i+1,j)))
                visited.add((i+1,j))
            if j<len(nums2)-1 and (i,j+1) not in visited:
                heappush(heap,(nums1[i]+nums2[j+1],[nums1[i],nums2[j+1]],(i,j+1)))
                visited.add((i,j+1))
            k-=1
        return res



        


        
        


        