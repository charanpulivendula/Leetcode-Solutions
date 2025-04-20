class Solution:
    def check(self, nums: List[int]) -> bool:
        new = sorted(nums)
        n = len(nums)
        for i in range(n):
            nums.append(nums.pop(0))
            if nums == new:
                return True
        return False

