from math import gcd
class Solution:
    def maxGCDScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        two_count = [0]*n
        for i,num in enumerate(nums):
            while(num and not num & 1):
                num = num>>1
                two_count[i]+=1
        res = 0

        for i in range(n):
            min_two_val = 35
            min_two_count = 0
            gcd_val = 0
            for j in range(i,n):
                gcd_val = gcd(gcd_val,nums[j])
                if min_two_val>two_count[j]:
                    min_two_val = two_count[j]
                    min_two_count = 1
                elif min_two_val==two_count[j]:
                    min_two_count+=1
                length = j-i+1
                if min_two_count<=k:
                    res = max(res,2*gcd_val*length)
                else:
                    res = max(res,gcd_val*length)
        
        return res




            
        