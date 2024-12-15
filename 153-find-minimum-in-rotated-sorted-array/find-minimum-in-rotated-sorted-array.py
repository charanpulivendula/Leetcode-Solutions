class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        mini = float('inf')
        while(l<=r):
            mid = (l+r)//2
            mini = min(mini,nums[mid])
            if nums[l]<=nums[mid]:
                if nums[l]<nums[r]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                if nums[l]>nums[r]:
                    r = mid - 1
                else:
                    l = mid+1
        return mini


                
