class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)

        hashset = set()
        left = 0
        right = 0
        maxLength = 0

        # sliding window
        while(left<len(s) and right<len(s)):
            if s[right] not in hashset:
                hashset.add(s[right])
            else:
                #pruning the window
                while(s[right] in hashset):
                    hashset.remove(s[left])
                    left+=1
            # tracking longest string
                hashset.add(s[right])
            maxLength = max(maxLength, right-left+1)

        # increasing size
            right+=1
            print(hashset)
        return  maxLength
