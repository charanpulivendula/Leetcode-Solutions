class Solution:
    def trap(self, height: List[int]) -> int:
        water = [0 for _ in range(len(height))]
        lmax = height[0]
        for i in range(1,len(height)):
            lmax = max(lmax,height[i])
            water[i] = lmax-height[i]
        rmax = height[-1]
        water[-1] = 0
        for i in range(len(height)-2,-1,-1):
            rmax = max(rmax,height[i])
            water[i] = min(water[i],rmax-height[i])
        
        return sum(water)