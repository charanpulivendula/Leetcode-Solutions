class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        j = 0
        count = 0
        print(g,s)
        while(i<len(g) and j<len(s)):
            if s[j]>=g[i]:
                i+=1
                count+=1
            j+=1
        return count
        