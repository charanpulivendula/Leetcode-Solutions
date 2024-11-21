class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # if n==1:
        #     return nums[0]
        # if n==2:
        #     return max(nums[0],nums[1])
        # dp = [0 for _ in range(n)]
        a = 0
        b = 0
        cash = 0
        

        for num in nums:
            cash = max(num+a,b)
            a = b
            b = cash
        
        return cash
