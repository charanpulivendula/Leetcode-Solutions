class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        resSet = []
        nums.sort()
        def recursion(arr,i):
            if i == len(nums):
                return
            if arr not in resSet:
                resSet.append(arr.copy())
            
            for j in range(i+1,len(nums)):
                arr.append(nums[j])
                recursion(arr,j)
                arr.pop()

        recursion([],-1)
        return resSet

        