from heapq import heappush,heappop,heapify
class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = []
        heapify(heap)
        res = ""
        for char in set(list(s)):
            heappush(heap,(-s.count(char),char))
        while(len(heap)>1):
            freq1,first = heappop(heap)
            freq2,second = heappop(heap)
            res += first
            res += second
            if freq1<-1:
                heappush(heap,(freq1+1,first))
            if freq2<-1:
                heappush(heap,(freq2+1,second))
        if heap:
            freq,final = heappop(heap)
            if freq<-1:
                return ""
            else:
                return res+final
        else:
            return res