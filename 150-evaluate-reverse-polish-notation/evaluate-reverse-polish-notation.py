class Solution(object):
    def evalRPN(self, tokens):
        stack=[]
        res=0
        print(abs(6)/abs(-132))
        for i in tokens:
            if i in "+-*/":
                val=self.operation(stack.pop(),stack.pop(),i)
                stack.append(val)
            else:
                stack.append(int(i))
        return stack.pop()

    def operation(self,val2,val1,oper):
        print(val1,val2)
        if oper == '+':
            return val1+val2

        elif oper == '-':
            return val1-val2

        elif oper == '*':
            return val1*val2
        
        elif oper == '/':
            return int(val1/val2)