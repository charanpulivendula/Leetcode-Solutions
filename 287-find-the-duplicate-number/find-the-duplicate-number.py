class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)
        slow = 0
        fast = 0
        while(True):
            slow = nums[slow]
            fast = nums[nums[fast]]
            print(slow,fast)
            if slow == fast:
                break
        slow = 0
        while(True):
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow