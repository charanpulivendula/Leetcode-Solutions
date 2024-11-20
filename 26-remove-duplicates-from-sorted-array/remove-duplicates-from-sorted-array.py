class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numSet = set()
        i = 0
        j = 0
        while(i<len(nums)):
            if nums[i] in numSet:
                i+=1
            else:
                numSet.add(nums[i])
                nums[j]=nums[i]
                j+=1
                i+=1
        return j
            
