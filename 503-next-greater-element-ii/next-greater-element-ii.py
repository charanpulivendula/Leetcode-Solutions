class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums2 = nums+nums
        stack = []
        hashmap = {}
        res = []
        for i in range(len(nums2)):
            while stack and nums2[i]>nums2[stack[-1]]:
                hashmap[stack.pop()] = nums2[i]
            stack.append(i)
        
        while stack:
            hashmap[stack.pop()]=-1

        counter = 0
        while(counter<n):
            res.append(hashmap[counter])
            counter+=1

        return res