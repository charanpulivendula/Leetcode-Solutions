class Solution:
    def countAndSay(self, n: int) -> str:
        #Base case
        if n == 1:
            return "1"
        
        #start from first tem
        result = "1"

        for _ in range(2,n+1):
            current = ""
            count = 1
            # process the previous term result
            for j in range(1,len(result)):
                if result[j] == result[j-1]:
                    count+=1
                else:
                    current+=str(count) + result[j-1]
                    count = 1
            # add the last counted digit
            current += str(count)+result[-1]

            result = current
        return result