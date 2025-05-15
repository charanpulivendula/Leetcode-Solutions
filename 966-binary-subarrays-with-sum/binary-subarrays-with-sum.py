class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashmap = defaultdict(int)
        pref_sum = 0
        hashmap[0] = 1
        counter = 0
        for num in nums:
            pref_sum+=num
            counter+=hashmap[pref_sum-goal]
            hashmap[pref_sum]+=1
        return counter

        