class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a,2)
        y = int(b,2)
        while y!=0:
            ans = x^y
            car = (x&y)<<1
            x,y = ans,car

        return bin(x)[2:]