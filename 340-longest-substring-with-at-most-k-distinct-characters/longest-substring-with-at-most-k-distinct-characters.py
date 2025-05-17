from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        longest = 0
        start = 0
        hashmap = defaultdict(int)
        for end in range(len(s)):
            hashmap[s[end]]+=1
            while len(hashmap)>k:
                hashmap[s[start]]-=1
                if hashmap[s[start]]==0:
                    del hashmap[s[start]]
                start+=1
            longest = max(longest,end-start+1)
        return longest
