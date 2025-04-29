from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)
        for char in s:
            freq[char]+=1
        d = sorted(freq.items(),key = lambda x:-x[1])
        res = ""
        for char in d:
            res+=char[0]*char[1]
        return res
