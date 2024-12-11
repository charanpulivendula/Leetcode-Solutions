class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            checker = 0
            for num in nums:
                checker += (num>>i)&1
            ans = checker%3
            res = res | ans<<i
        if res >= (1<<31):
            res -= (1<<32)
        return res