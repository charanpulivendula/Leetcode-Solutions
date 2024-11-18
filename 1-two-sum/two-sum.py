class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = dict()
        for i,num in enumerate(nums):
            if target-num in numsDict:
                return [i,numsDict[target-num]]
            numsDict[num] = i