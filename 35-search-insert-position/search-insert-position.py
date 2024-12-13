class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        mid = -1
        if target>nums[-1]:
            return len(nums)
        if target <nums[0]:
            return 0
        if len(nums)<=1:
            return 0
        while(i<=j):
            mid = (i+j)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                j = mid-1
            else:
                i=mid+1
            # print(i,j)
        return i
