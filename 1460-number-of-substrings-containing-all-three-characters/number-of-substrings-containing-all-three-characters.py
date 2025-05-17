from collections import defaultdict
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        hashmap = defaultdict(int)
        n = len(s)
        start = 0
        for end in range(n):
            hashmap[s[end]]+=1
            while(len(hashmap)==3):
                hashmap[s[start]]-=1
                if hashmap[s[start]] == 0:
                    del hashmap[s[start]]
                start+=1
                count+=(n-end)
            print(count)
        return count
