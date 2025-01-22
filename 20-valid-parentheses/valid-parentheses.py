class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')':'(','}':'{',']':'['}
        #stack to store opening brackets
        stack = []
        for char in s:
            if char in bracket_map:
                if stack and stack[-1] == bracket_map[char]:
                    #removing the matching opening bracket
                    stack.pop()
                else:
                    return False
            else:
                #push open bracket to stack
                stack.append(char)
            
        return not stack

        