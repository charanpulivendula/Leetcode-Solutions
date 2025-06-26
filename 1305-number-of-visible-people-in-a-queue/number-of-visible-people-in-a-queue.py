class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(heights))]
        for i,height in enumerate(heights):
            while stack and heights[stack[-1]]<height:
                popped_index = stack.pop()
                res[popped_index] += 1
            if stack:
                res[stack[-1]]+=1
            stack.append(i)
        return res
