class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        maxi =  float('-inf')
        for i in range(len(number)-1):
            if number[i] == digit:
                maxi = max(maxi,int(number[:i]+number[i+1:]))
        if number[-1]==digit:
            maxi = max(maxi,int(number[:-1]))
        return str(maxi)
