class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        i = 1
        intervals.sort(key = lambda x:x[0])
        while(i<len(intervals)):
            left = max(intervals[i-1][0],intervals[i][0])
            right = min(intervals[i-1][1],intervals[i][1])
            if left<=right:
                intervals[i] = [min(intervals[i-1][0],intervals[i][0]),max(intervals[i-1][1],intervals[i][1])]
            else:
                res.append(intervals[i-1])
            i+=1
        res.append(intervals[i-1])
        return res


        