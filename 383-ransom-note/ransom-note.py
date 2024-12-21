from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False
        hashed = defaultdict(int)
        for char in magazine:
            hashed[char]+=1
        for char in ransomNote:
            hashed[char]-=1
        for _,value in hashed.items():
            if value < 0:
                return False
        return True
        
        