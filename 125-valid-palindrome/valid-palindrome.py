class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = "0123456789abcdefghijklmnopqrstuvwxyz"
        i = 0
        j = len(s)-1
        while(i<j):
            
            if s[i].lower() not in valid:
                i+=1
                continue

            if s[j].lower() not in valid:
                j-=1
                continue

            if s[i].lower()!=s[j].lower():
                return False
            else:
                i+=1
                j-=1
        return True
        