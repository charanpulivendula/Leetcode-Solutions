class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n < 10 or n >= 2**31:
            return -1
        string = list(map(int,str(n)))
        index = len(string)-1
        for i in range(len(string)-1,0,-1):
            if int(string[i])>int(string[i-1]):
                index = i-1
                break
        mini = float('inf')
        for i in range(len(string)-1,index,-1):
            if int(string[i])>int(string[index]):
                string[index],string[i] = string[i],string[index]
                break

        # print(string[:index+1]+sorted(string[index+1])
        res = int("".join(map(str,string[:index+1]))+"".join(map(str,sorted(string[index+1:]))))
        print(2**31,res)
        if n == res or res >=2**31:
            return -1
        else:
            return res
