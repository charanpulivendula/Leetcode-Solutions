from queue import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque([0])
        for i in range(1,k):
            while (q and nums[i]>nums[q[-1]]):
                q.pop()
            q.append(i)
        res.append(nums[q[0]])
        print(q)
        for i in range(k,len(nums)):
            if q and q[0]==i-k:
                q.popleft()
            while (q and nums[i]>nums[q[-1]]):
                q.pop()
            q.append(i)
            
            res.append(nums[q[0]])
        return res
            