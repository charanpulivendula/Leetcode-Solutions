class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums)-1
        while(start<=end):
            mid = (start+end)//2
            if nums[mid]==target:
                return True

            if nums[start] == nums[mid] == nums[end]:
                start += 1
                end -= 1
            elif nums[mid]>=nums[start]:
                if nums[start]<=target<nums[mid]:
                    end = mid - 1
                else:
                    start = mid+1
            else:
                if nums[mid]<target<=nums[end]:
                    start = mid+1
                else:
                    end = mid - 1
        return False
                    