class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = defaultdict(int)
        start = 0
        maxisum = 0
        for end in range(len(fruits)):
            d[fruits[end]]+=1
            while(start<end and len(d)>2):
                d[fruits[start]]-=1
                if d[fruits[start]]==0:
                    del d[fruits[start]]
                start+=1
            maxisum = max(maxisum,end-start+1)
        return maxisum
