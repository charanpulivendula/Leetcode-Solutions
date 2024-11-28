class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        longest = s[0:1]
        for i in range(n):
            dp[i][i] = True
        for i in range(n-1):
            dp[i][i+1] = s[i]==s[i+1]

        for j in range(n):
            for i in range(j):
                if j!=i+1:
                    dp[i][j] = s[i]==s[j] and dp[i+1][j-1]
                if dp[i][j]:
                    if j-i+1 > len(longest):
                        longest = s[i:j+1] 
        return longest
