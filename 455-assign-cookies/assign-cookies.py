class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        m = len(g)
        n = len(s)
        g.sort()
        s.sort()
        i = 0
        j = 0
        while(i<m and j<n):
            if g[i]<=s[j]:
                i+=1
                count+=1
            j+=1
        return count

            
        