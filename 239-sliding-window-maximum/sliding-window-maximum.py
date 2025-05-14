from queue import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque([0])
        n = len(nums)
        res = []
        for i in range(1,k):
            while queue and nums[queue[-1]]<nums[i]:
                queue.pop()
            queue.append(i)
        res.append(nums[queue[0]])
        for i in range(k,n):
            if queue and queue[0]==i-k:
                queue.popleft()
            while(queue and nums[queue[-1]]<nums[i]):
                queue.pop()
            queue.append(i)
            res.append(nums[queue[0]])
        return res
