from heapq import heappush,heappop
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        heap = []
        for i in range(m):
            heappush(heap,nums1[i])

        for i in range(n):
            heappush(heap,nums2[i])
        
        for i in range(len(nums1)):
            nums1[i] = heappop(heap)
        return nums1
        