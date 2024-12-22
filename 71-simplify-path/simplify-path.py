class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        temp_string = ""
        path+="/"
        for char in path:
            if char=="/":
                if temp_string=="" or temp_string == ".":
                    pass
                elif temp_string == "..": 
                    if stack:
                        stack.pop()
                        stack.pop()
                else:
                    stack.append(temp_string)
                    stack.append("/")
                temp_string = ""
            else:
                temp_string+=char
        if temp_string:
            print(temp_string)
            stack.append(temp_string)
        if stack and stack[-1]=="/":
            stack.pop()
        # if not stack:
        #     stack.append("/")
        # if stack[0]!="/":
    
        return "/"+"".join(stack)
        