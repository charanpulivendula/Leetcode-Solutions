class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cache_word = defaultdict(str)
        cache_char = defaultdict(str)
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in cache_word:
                if cache_word[s[i]]!=t[i]:
                    return False
            if t[i] in cache_char:
                if cache_char[t[i]]!=s[i]:
                    return False
            cache_word[s[i]]=t[i]
            cache_char[t[i]]=s[i]
                    
        return True