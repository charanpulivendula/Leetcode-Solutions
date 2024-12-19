class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = sum(nums)
        n = len(nums)
        if target>s:
            return 0
        elif target == s:
            return len(nums)
        i = 0
        j = 0
        cursum = 0
        window = float('inf')
        while(i<n and j<n):
            cursum += nums[j]
            while(cursum>=target):
                cursum -= nums[i]
                window = min(window,j-i+1)
                i+=1
            j+=1
            
        return window

        