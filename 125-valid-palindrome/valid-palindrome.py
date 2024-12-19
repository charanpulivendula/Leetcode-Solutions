class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        i = 0
        j = len(s)-1
        while(i<j):
            
            while i<len(s) and s[i] not in valid:
                i+=1

            while j>=0 and s[j] not in valid:
                j-=1

            if i<len(s) and j>=0 and s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1
        return True
        