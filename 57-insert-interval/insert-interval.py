class Solution:
    def insert(self, interval: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if interval == []:
            return [newInterval]
        res = []
        l = 0
        r = len(interval)-1
        while(l<=r):
            mid = (l+r)//2
            if interval[mid][0]>=newInterval[0]:
                r = mid-1
            else:
                l = mid+1
        res = []
        i = 1
        while(i<l):
            left = max(interval[i-1][0],interval[i][0])
            right = min(interval[i-1][1],interval[i][1])
            if left<=right:
                interval[i] = [min(interval[i-1][0],interval[i][0]),max(interval[i-1][1],interval[i][1])]
            else:
                res.append(interval[i-1])
            i+=1
        i-=1
        lmax = max(interval[i][0],newInterval[0])
        rmin = min(interval[i][1],newInterval[1])
        if lmax<=rmin:
                interval[i] = [min(interval[i][0],newInterval[0]),max(interval[i][1],newInterval[1])]
        else:
            res.append(interval[i])
            interval[i] = newInterval
        i+=1
        while(i<len(interval)):
            left = max(interval[i-1][0],interval[i][0])
            right = min(interval[i-1][1],interval[i][1])
            if left<=right:
                interval[i] = [min(interval[i-1][0],interval[i][0]),max(interval[i-1][1],interval[i][1])]
            else:
                res.append(interval[i-1])
            i+=1
        res.append(interval[i-1])
        res.sort()
        return res
        


                