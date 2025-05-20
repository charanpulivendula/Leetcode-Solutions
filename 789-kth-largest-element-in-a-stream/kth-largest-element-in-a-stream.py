from heapq import heappush,heappop,heapify
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            heappush(self.heap,num)
        while (len(self.heap)>k):
            heappop(self.heap)


    def add(self, val: int) -> int:
        heappush(self.heap,val)
        if len(self.heap)>self.k:
            heappop(self.heap)        
        res = heappop(self.heap)
        heappush(self.heap,res)
        return res

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)