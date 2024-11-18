class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        numSet = set(nums)
        totalSet = set(range(1,len(nums)+1))
        return list(totalSet-numSet)
        