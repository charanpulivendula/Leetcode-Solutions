class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index = -1
        l = 0
        r = len(nums)-1
        def search(l,r):
            if l>r:
                return [-1,-1]

            if nums[l] == target and nums[r] == target:
                return [l,r]

            mid = (l+r)//2

            if nums[mid]==target:
                if nums[l]!=target:
                    return search(l+1,r)
                else:
                    return search(l,r-1)

            if nums[mid]<target:
                return search(mid+1,r)
                
            elif nums[mid]>target:
                return search(l,mid-1)

        while(l<=r):
            mid = (l+r)//2
            if nums[mid] == target:
                return search(l,r)

            elif nums[mid]>target:
                r = mid-1

            else:
                l = mid+1
        return [-1,-1]