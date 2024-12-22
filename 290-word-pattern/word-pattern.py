from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        cache_word = defaultdict(str)
        cache_char = defaultdict(str)
        s_array = s.split(" ")
        if len(s_array)!=len(pattern):
            return False
        for i in range(len(s_array)):
            if s_array[i] in cache_word:
                if cache_word[s_array[i]]!=pattern[i]:
                    return False
            if pattern[i] in cache_char:
                if cache_char[pattern[i]]!=s_array[i]:
                    return False
            cache_word[s_array[i]]=pattern[i]
            cache_char[pattern[i]]=s_array[i]
                    
        return True

        