class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def isoverlapping(a,b):
            return max(a[0],b[0])<min(a[1],b[1])
        intervals.sort()
        i = 0
        j = 1
        count = 0
        n = len(intervals)
        end = intervals[0][1]
        for i in range(1,len(intervals)):

            if intervals[i][0]<end:
                count+=1
                end = min( intervals[i][1],end)
            else:
                end = intervals[i][1]
        return count

