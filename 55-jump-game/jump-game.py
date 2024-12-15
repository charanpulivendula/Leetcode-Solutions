class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1
        index = target-1
        while(index>=0):
            if nums[index]+index>=target:
                target = index
            index-=1
        return target == 0
