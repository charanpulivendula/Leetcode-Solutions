class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        for end in range(len(s)):
            freq = defaultdict(int)
            for start in range(end,len(s)):
                freq[s[start]]+=1
                values = freq.values()
                ans += max(values)-min(values) if values else 0
                print(ans)

        return ans
            
                
