from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_dict =defaultdict(int)
        t_dict =  defaultdict(int)
        formed = 0
        res = ""
        minleng =  float('inf')
        start = 0
        for elem in t:
            t_dict[elem]+=1
        req = len(t_dict)
        for end in range(len(s)):
            s_dict[s[end]]+=1
            if s[end] in t_dict and  s_dict[s[end]]==t_dict[s[end]]:
                formed+=1
            while formed == req:
                leng = end-start+1
                if leng<minleng:
                    minleng = min(leng,minleng)
                    res = s[start:end+1]
                if s[start] in t_dict and s_dict[s[start]]==t_dict[s[start]]:
                    formed-=1
                s_dict[s[start]]-=1
                start+=1

        return res
            
