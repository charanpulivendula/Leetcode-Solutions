class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while(nums and i<len(nums)):
            if nums[i] == val:
                nums.pop(i)
            else:
                i+=1
        return len(nums)
        