class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numStore = [0]*101

        for num in nums:
            numStore[num] += 1
        
        for i in range(1,len(numStore)):
            numStore[i]+=numStore[i-1]
        
        numStore.append(0)

        return [numStore[num-1] for num in nums]
        