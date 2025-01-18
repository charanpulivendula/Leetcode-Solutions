class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        resSet = []
        def recursion(arr,i):
            if i == len(nums):
                return
            new = sorted(arr)
            if new not in resSet:
                resSet.append(new)
            for j in range(i+1,len(nums)):
                temp = arr.copy()
                temp.append(nums[j])
                recursion(temp,j)

        recursion([],-1)
        return list(sorted(resSet))

        