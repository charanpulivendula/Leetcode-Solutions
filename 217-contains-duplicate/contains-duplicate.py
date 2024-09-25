class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l = set(nums)
        return len(l)!=len(nums)
        
        