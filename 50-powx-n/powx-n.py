class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        flag = True
        if(n<0):
            n = -1*n
            x = 1/x
        while(n):
            if n%2 == 1:
                res *=x
                n-=1
            x=x*x
            n//=2
        return res

        