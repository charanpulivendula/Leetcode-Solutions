class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        right = [1 for _ in range(n)]
        right[-1] = nums[-1]
        for i in range(n-2,-1,-1):
            right[i] = right[i+1]*nums[i]
        right.append(1)
        res = []
        # print(right)
        left = 1
        for i in range(n):
            res.append(left*right[i+1])
            left*=nums[i]
        return res

