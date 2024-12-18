class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""
        s = s.lstrip()
        s = s.rstrip()
        s = " "+s
        i = len(s)-1
        tempstr = ''
        while(i>=0):
            if s[i]==" ":
                res += tempstr[::-1]+" "
                tempstr = ""
                while(i>=0 and s[i]==" "):
                    i-=1
            tempstr+=s[i]
            i-=1
        
        return res.rstrip()
        
