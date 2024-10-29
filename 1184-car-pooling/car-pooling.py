class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        last = 0
        for trip in trips:
            last = max(last,trip[2])
        passengers = [0]*(last+1)
        for trip in trips:
            passengers[trip[1]] += trip[0]
            passengers[trip[2]] += -trip[0]
        maxi = passengers[0]
        print(passengers)
        for i in range(1,len(passengers)):
            passengers[i] += passengers[i-1]
            maxi = max(maxi,passengers[i])
            if maxi > capacity:
                return False
            
        return True
        