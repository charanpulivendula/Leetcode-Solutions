from heapq import heappush as push,heappop as pop
class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        heappush(self.minheap,num)
        heappush(self.maxheap,-heappop(self.minheap))
        if len(self.maxheap)>len(self.minheap):
            heappush(self.minheap,-heappop(self.maxheap))
        

    def findMedian(self) -> float:
        res = 0
        if len(self.maxheap)==len(self.minheap):
            first = -pop(self.maxheap)
            second = pop(self.minheap)
            res = (first+second)/2
            push(self.maxheap,-first)
            push(self.minheap,second)
        else:
            res = pop(self.minheap)
            push(self.minheap,res)
        return res
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()