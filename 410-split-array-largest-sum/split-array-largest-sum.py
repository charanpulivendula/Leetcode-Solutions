class Solution:
    def splitArray(self, arr: List[int], k: int) -> int:
        if len(arr)<k:
            return -1
        def numpages(x):
            counter = 1
            total = 0
            for elem in arr:
                if total+elem>x:
                    total = 0
                    counter+=1
                total+=elem
            return counter
        start = max(arr)
        end = sum(arr)
        while(start<end):
            mid = (start+end)//2
            students = numpages(mid)
            if students > k:
                start = mid+1
            else:
                end = mid
        return start