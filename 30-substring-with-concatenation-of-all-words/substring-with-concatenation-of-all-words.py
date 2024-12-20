class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        required = len(words[0])*len(words)
        each = len(words[0])
        words.sort()
        def checkvalidation(i,j):
            string = s[i:j]
            split_array = []
            l = 0
            r = each
            while(l<len(string) and r<=len(string)):
                split_array.append(string[l:r])
                l+=each
                r+=each
            return sorted(split_array) == words
        
        i = 0
        j = required
        res = []
        while(i<len(s) and j<=len(s)):
            if checkvalidation(i,j):
                res.append(i)

            i+=1
            j+=1
        return res
