class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        cash1 = 0
        a = 0
        b = 0
        for num in nums[1:]:
            cash1 = max(a+num,b)
            a = b
            b = cash1

        cash2= 0
        x=0
        y=0
        for num in nums[:-1]:
            cash2 = max(x+num,y)
            x = y
            y = cash2
        return max(b,y)