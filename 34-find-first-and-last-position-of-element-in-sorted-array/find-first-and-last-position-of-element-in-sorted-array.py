class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index = -1
        l = 0
        r = len(nums)-1
        left = -1
        right = -1
        while(l<=r):
            mid = (l+r)//2
            if nums[mid] == target:
                left = mid
                r = mid - 1 

            elif nums[mid]>target:
                r = mid-1

            else:
                l = mid+1

        l = 0
        r = len(nums)-1
        while(l<=r):
            mid = (l+r)//2
            if nums[mid] == target:
                right = mid
                l = mid + 1

            elif nums[mid]>target:
                r = mid-1

            else:
                l = mid+1

        return [left,right]