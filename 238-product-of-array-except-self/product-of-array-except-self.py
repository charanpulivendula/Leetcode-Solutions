class Solution:
    def productExceptSelf(self, nums):
        if len(nums) == 1:
            return len(nums)

        prefix = [1]*len(nums)
        postfix = [1]*len(nums)
        prefix[0] = nums[0]
        postfix[-1] = nums[-1]
        result = [1]*len(nums)

        n = len(nums)
        for i in range(1,len(nums)):
            prefix[i] = nums[i]*prefix[i-1]
            postfix[n-i-1] = nums[n-i-1]*postfix[n-i]
        
        result[0] = postfix[1]
        result[-1] = prefix[-2]
        
        for i in range(1,len(result)-1):
            result[i] = prefix[i-1]*postfix[i+1]
        return result
            

        