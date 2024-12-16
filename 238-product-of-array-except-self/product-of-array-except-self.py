class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        right = 1 
        res = []
        # print(right)
        left = 1
        for i in range(n):
            res.append(left)
            left*=nums[i]
        for i in range(n-1,-1,-1):
            res[i]*=right
            right *= nums[i]
        return res

