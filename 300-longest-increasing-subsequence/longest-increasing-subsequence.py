class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(len(dp)):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i],1+dp[j])
        return max(dp)
        