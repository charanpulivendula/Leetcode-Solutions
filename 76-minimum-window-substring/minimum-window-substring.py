from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def equal(dict1,dict2):
            if len(dict1)!=len(dict2):
                return False
            for char in dict1:
                if dict1[char]!=dict2[char]:
                    return False
            return True

        if len(s)<len(t):
            return ""
        if s==t:
            return s
        cache = defaultdict(int)
        cur_dict = defaultdict(int)
        for char in t:
            cache[char]+=1
        formed = 0
        i = 0
        j = 0
        minlength = float('inf')
        required = len(cache)
        minstr = ""
        while(i<len(s) and j<len(s)):
            if s[j] in cache:
                cur_dict[s[j]]+=1
                if cur_dict[s[j]]==cache[s[j]]:
                    formed+=1
            # print(cur_dict)
            while(i<=j and formed == required):
                if j-i+1 < minlength:
                    minlength = j-i+1
                    minstr = s[i:j+1]
                if s[i] in cur_dict:
                    cur_dict[s[i]]-=1
                    if cur_dict[s[i]]<cache[s[i]]:
                        formed-=1
                i+=1
            j+=1


        return minstr
            
