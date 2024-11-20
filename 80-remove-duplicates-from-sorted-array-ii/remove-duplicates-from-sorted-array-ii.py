class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 1
        prev = nums[0]
        i = 1
        j = 1
        while(i<len(nums)):
            if nums[i] == prev:
                counter+=1
            else:
                counter = 1
            if counter <=2:
                prev = nums[i]
                if i!=j:
                    nums[j] = nums[i]
                j+=1
            else:
                while(nums[i]!=prev):
                    i+=1
            i+=1
        return j

                
                 

        