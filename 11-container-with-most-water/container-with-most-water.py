class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        water = float('-inf')
        while(i < j):
            water = max(water,(j-i)*min(height[i],height[j]))
            if height[i] >= height[j]:
                j-=1
            else:
                i+=1
        
        return water
                
