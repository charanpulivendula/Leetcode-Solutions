class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack= []
        for char in num:
            while stack and stack[-1]>char and k:
                stack.pop()
                k-=1
            stack.append(char)
        while(k and stack):
            stack.pop()
            k-=1
        res = ""
        for char in stack:
            res = res+char
        res = res.lstrip("0")
        if res == "":
            return "0"
        else:
            return res



        