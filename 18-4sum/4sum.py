class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def ksum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []
            if not nums:
                return res
            avg_value = target // k
            if avg_value < nums[0] or nums[-1] < avg_value:
                return res
            if k == 2:
                return twosum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in ksum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)
            return res
        def twosum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            lo, hi = 0,len(nums) - 1
            while (lo < hi):
                curr_sum = nums[lo] + nums[hi]
                if curr_sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif curr_sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo],nums[hi]])
                    lo += 1
                    hi -= 1
            return res
        nums.sort()
        return ksum(nums,target,4)