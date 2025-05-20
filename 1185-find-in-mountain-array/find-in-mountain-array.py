# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, nums: 'MountainArray') -> int:
        n = nums.length()
        left = 0
        right = n-1
        peak = 0
        while(left<=right):
            mid = (left+right)//2
            i = nums.get(mid-1) if mid>0 else -1
            j = nums.get(mid+1) if mid<n-1 else -1
            midval = nums.get(mid)
            if i<=midval and midval>=j:
                peak = mid
                break
            elif i<=nums.get(mid):
                left = mid+1
            else:
                right= mid - 1
        left = 0
        right = peak
        while(left<=right):
            mid = (left+right)//2
            midval = nums.get(mid)
            if midval==target:
                return mid
            elif midval>target:
                right = mid-1
            else:
                left = mid+1 

        left = peak
        right = n-1
        while(left<=right):
            mid = (left+right)//2
            midval = nums.get(mid)
            if midval==target:
                return mid
            elif midval>target:
                left = mid+1
            else:
                 right = mid-1
        return -1

