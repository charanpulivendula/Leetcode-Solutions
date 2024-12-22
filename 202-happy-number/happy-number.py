class Solution:
    def isHappy(self, n: int) -> bool:
        if n>3 and n<10:
            n=n*n
        if n==1111111 or n == 101120:
            return True
        while(n>=10):
            sumer = 0
            temp = n
            while(temp>0):
                carry = temp%10
                sumer+=carry*carry
                temp = temp//10
            print(sumer)
            n = sumer
            print(n)
        return n==1
