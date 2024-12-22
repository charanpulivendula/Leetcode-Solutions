from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cache = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in cache:
                if abs(i-cache[nums[i]])<=k:
                    return True
            cache[nums[i]] = i
        return False
        