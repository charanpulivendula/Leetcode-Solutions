class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        index = len(nums)-k
        nums[:] = (nums[:index][::-1]+nums[index:][::-1])[::-1]
        
        return nums
        