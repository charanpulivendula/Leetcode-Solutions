class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while(l<=r):
            if l==r:
                return l
            mid = (l+r)//2
            if nums[mid]<nums[mid+1]:
                l = mid+1
            else:
                r = mid
        return l