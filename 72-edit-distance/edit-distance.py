class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        m = len(word1)
        n = len(word2)
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        print(dp)
        
        return dp[m][n]