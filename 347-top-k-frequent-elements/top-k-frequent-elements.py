from heapq import heappush,heappop
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num]+=1
        for (num,freq) in hashmap.items():
            heappush(heap,(freq,num))
            if len(heap)>k:
                heappop(heap)
        res = []
        while(heap):
            res = [heappop(heap)[1]]+res
        return res