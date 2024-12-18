class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.rstrip()
        s = s.lstrip()
        words = s.split(" ")
        print(words)
        res = ""
        for word in words:
            if word:
                res = word+" "+res
        return res.rstrip()
        
