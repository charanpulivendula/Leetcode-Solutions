class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        lprod = [1,nums[0]]
        laccum = nums[0]
        rprod = [1 for _ in range(n+1)]
        rprod[-2] = nums[-1]
        raccum = nums[-1]
        for i in range(1,n):
            lprod.append(nums[i]*laccum)
            laccum = nums[i]*laccum

        for i in range(n-2,-1,-1):
            rprod[i] = raccum*nums[i]
            raccum*=nums[i]
        res = []
        # print(lprod)
        # print(rprod)
        for i in range(1,n+1):
            res.append(lprod[i-1]*rprod[i])
        
        return res
