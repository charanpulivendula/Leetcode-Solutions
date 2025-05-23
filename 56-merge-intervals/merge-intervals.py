class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        i = 1
        intervals.sort()
        last = intervals[0]
        while(i<len(intervals)):
            left = max(last[0],intervals[i][0])
            right = min(last[1],intervals[i][1])
            if left<=right:
                last = [min(last[0],intervals[i][0]),max(last[1],intervals[i][1])]
            else:
                res.append(last)
                last = intervals[i]
            i+=1
        res.append(last)
        return res


        