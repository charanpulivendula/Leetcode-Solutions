class Solution(object):
  def longestPalindrome(self, s):
      """
      :type s: str
      :rtype: str
      """
      if len(s) < 1:
        return s

      dp = [[False for i in range(len(s))] for j in range(len(s))]

      longest = ""

      for i in range(len(s)):
        dp[i][i] = True
        longest = s[i]

      for i in range(len(s)):
        for j in range(i):
          if s[i] == s[j]:
            if i == j+1 or dp[j+1][i-1]:
              dp[j][i] = True
              if len(longest) < len(s[j:i+1]):
                longest = s[j:i+1]

      return longest