
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        alpha = [0]*26
        for i in tasks:
            alpha[ord(i)-ord('A')]+=1
        alpha.sort()
        maxi = alpha.pop()
        length = 0
        vacancy = (maxi-1)*n
        while(alpha):
            temp = alpha.pop()
            vacancy -= min(temp,maxi-1)
        if vacancy>0:
            return len(tasks)+vacancy
        else:
            return len(tasks)


        