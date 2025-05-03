class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def recursion(n):
            if n==1:
                return 5
            if n == 2:
                return 20
            carry = n%2
            return (pow(20,n//2,10**9+7)*pow(5,carry))%(10**9+7)

        return recursion(n)