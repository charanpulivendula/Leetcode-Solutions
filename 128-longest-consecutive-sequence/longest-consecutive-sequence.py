from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = [5,4,3,2,1,100]
        num_set = set(nums)
        visited = set()
        maxcount = 0
        for num in nums:
            count = 1
            if num not in visited:
                temp = num
                visited.add(num)
                while(temp-1 in num_set):
                    count+=1
                    visited.add(temp-1)
                    temp-=1
                temp = num
                while(temp+1 in num_set):
                    count+=1
                    visited.add(temp+1)
                    temp+=1
            maxcount = max(maxcount,count)
        # print(visited)
        return maxcount
            


        

