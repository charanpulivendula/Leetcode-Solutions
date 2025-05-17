class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def findnice(x):
            start = 0
            count = 0
            n = len(nums)
            oddcount = 0
            for end in range(n):
                if nums[end]%2 == 1:
                    oddcount+=1
                while  oddcount>x:
                    if nums[start]%2==1:
                        oddcount-=1
                    start+=1
                count+=end-start+1

            return count
        return findnice(k)-findnice(k-1)