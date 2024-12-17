class Solution:
    def candy(self, ratings: List[int]) -> int:
        choco = [1 for _ in range(len(ratings))]
        count = 1
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                count+=1
                choco[i] = count
            else:
                count = 1
        count = choco[-1]
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                count+=1
                choco[i] = max(choco[i],count)
            else:
                count = 1
        print(choco)
        return sum(choco)
