class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        final = primeOne*primeTwo
        dp = [False for _ in range(final+1)]
        dp[primeOne] = True
        dp[primeTwo] = True
        for i in range(final+1):
            if dp[i] and i+primeOne<=final:
                dp[i+primeOne] = True
            if dp[i] and i+primeTwo<=final:    
                dp[i+primeTwo] = True
        
        for i in range(len(dp)-1,0,-1):
            if not dp[i]:
                return i

                    


        