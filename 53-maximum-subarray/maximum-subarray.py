class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxSum = -999999
        localMax = -9999999
        for i in range(len(nums)):
            localMax = max(nums[i],localMax+nums[i])
            if localMax > maxSum:
                maxSum = localMax
        return maxSum
