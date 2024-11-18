class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            try:
                return [(nums[:i] + nums[i+1 :]).index(target-n)+1, i]
            except:
                pass