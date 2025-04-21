class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        j = 1
        while i<len(nums):
            if nums[i]!=nums[i-1]:
                nums[j] = nums[i]
                i+=1
                j+=1
            else:
                i+=1
        return j
        
