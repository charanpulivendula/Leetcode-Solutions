class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        prefix = [0]*n
        prefix[0]=cardPoints[0]
        
        for i in range(1,n):
            prefix[i] = prefix[i-1]+cardPoints[i]
        maxi = prefix[n-1]-prefix[n-k-1]
        for i in range(k):
            offset = k-i-1
            print(offset)
            maxi = max(maxi,prefix[i]+prefix[n-1]-prefix[n-offset-1])
        return maxi

            

        