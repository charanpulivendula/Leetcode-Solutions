class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if len(digits)==0:
            return []
        digit_map = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        def backtrack(i,s):
            if i==len(digits):
                res.append(s)
                return
            digit = int(digits[i])
            for char in digit_map[digit]:
                s+=char
                backtrack(i+1,s)
                s = s[:-1]
        
        backtrack(0,"")
        return res
            
        