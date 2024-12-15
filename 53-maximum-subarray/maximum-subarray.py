class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        agg = nums[0]
        maxi = nums[0]
        for i in range(1,len(nums)):
            agg = max(agg+nums[i],nums[i])
            maxi = max(agg,maxi)
        return maxi