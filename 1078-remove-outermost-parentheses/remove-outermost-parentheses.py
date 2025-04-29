class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        val = 0
        res = ""
        for char in s:
            if char == "(":
                if val>0:
                    res+=char
                val+=1
            else:
                val-=1
                if val>0:
                    res+=char
        return res