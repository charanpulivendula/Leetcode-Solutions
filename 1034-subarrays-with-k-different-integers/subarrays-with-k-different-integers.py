from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def findKDistinct(x):
            start = 0
            hashmap = defaultdict(int)
            count = 0
            n = len(nums)
            for end in range(n):
                hashmap[nums[end]]+=1
                while(len(hashmap)>x):
                    hashmap[nums[start]]-=1
                    if hashmap[nums[start]]==0:
                        del hashmap[nums[start]]
                    start+=1
                count+=end-start+1
            return count
        return findKDistinct(k)-findKDistinct(k-1)