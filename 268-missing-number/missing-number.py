class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsSet = set(nums)
        i = 0
        while(i<len(nums)):
            if i not in numsSet:
                return i
            i+=1

        return i
        