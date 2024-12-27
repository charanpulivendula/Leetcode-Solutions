class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 1
        candidate = nums[0]
        for i in range(1,len(nums)):
            if counter == 0:
                candidate = nums[i]
                counter+=1
            else:
                if candidate == nums[i]:
                    counter+=1
                else:
                    counter-=1

        return candidate

