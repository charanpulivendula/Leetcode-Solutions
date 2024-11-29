class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        memcache = {}

        def recursion(i, j):
            # Check the cache
            if (i, j) in memcache:
                return memcache[(i, j)]
            
            # Base case: if both strings are fully used
            if i == len(s1) and j == len(s2):
                return True
            
            # Compare characters directly with s3
            ans = False
            if i < len(s1) and s1[i] == s3[i + j]:
                ans |= recursion(i + 1, j)
            if j < len(s2) and s2[j] == s3[i + j]:
                ans |= recursion(i, j + 1)
            
            # Cache and return the result
            memcache[(i, j)] = ans
            return ans

        return recursion(0, 0)