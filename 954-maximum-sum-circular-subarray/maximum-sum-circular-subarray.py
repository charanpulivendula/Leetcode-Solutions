class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        agg = nums[0]
        maxi = nums[0]
        for i in range(1,len(nums)):
            agg = max(agg+nums[i],nums[i])
            maxi = max(agg,maxi)

        agg = nums[0]
        mini = nums[0]
        for i in range(1,len(nums)):
            agg = min(agg+nums[i],nums[i])
            mini = min(agg,mini)
        
        total = sum(nums)
        if total == mini:
            return maxi
        return max(maxi,total-(1*mini))