class Solution:
    def hIndex(self, citations: List[int]) -> int:
        dp = [0]*1001
        for cite in citations:
            dp[cite] += 1

        count = 0
        for i in range(1000,-1,-1):
            dp[i]+=count
            count = dp[i]
            
                
        print(dp)
        for i in range(len(dp)-1,-1,-1):
            if dp[i] and dp[i]>=i:
                return i
        
