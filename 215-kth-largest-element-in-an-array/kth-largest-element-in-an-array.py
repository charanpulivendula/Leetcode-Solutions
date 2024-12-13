from heapq import heappush,heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap,-1*num)
        print(heap)
        res = -1
        while k>0:
            res = heappop(heap)
            k-=1
        return -1*res