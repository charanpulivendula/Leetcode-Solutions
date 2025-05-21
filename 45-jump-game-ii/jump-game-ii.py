class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf') for _ in range(len(nums))]
        dp[0] = 0
        for i in range(1,len(dp)):
            for j in range(i):
                if nums[j]+j>=i:
                    dp[i] = min(dp[i],1+dp[j])
                    # break
        return dp[len(dp)-1]
                    
    