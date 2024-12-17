class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mini = min(strs)
        maxi = max(strs)
        ans= ''
        for i in range(len(mini)):
            if mini[i]!=maxi[i]:
                break
            ans+=mini[i]
        return ans