class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        n = len(cost)
        diff_array = [gas[i]-cost[i] for i in range(n)]
        maxi = float('-inf')
        total = 0
        index = 0
        for i,diff in enumerate(diff_array):
            total+=diff
            if total<0:
                index = i+1
                total = 0
        return index

        