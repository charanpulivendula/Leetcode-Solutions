from collections import defaultdict
from heapq import heappush,heappop
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n  = len(hand)
        if n%groupSize!=0:
            return False
        def isvalid(arr):
            for i in range(1,len(arr)):
                if arr[i][0]-arr[i-1][0]!=1:
                    return False
            return True
        heap = []
        hashmap = defaultdict(int)
        for card in hand:
            hashmap[card]+=1
        
        for key,val in hashmap.items():
            heappush(heap,(key,val))
        count = 0
        while(heap):
            if len(heap)<groupSize:
                return False
            s = []
            for _ in range(groupSize):
                elem = heappop(heap)
                s.append(elem)
            
            if not isvalid(s):
                return False
            for key,val in s:
                if val>1:
                    heappush(heap,(key,val-1))
        return True
            

                    
                
        

        