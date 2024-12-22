class Solution:
    def isValid(self, s: str) -> bool:
        listt = []
        open = ['(','{','[']
        mapp = {')':'(','}':'{',']':'['}
        if s == '':
            return True
        for i in range(len(s)):
            if s[i] in open:
                listt.append(s[i])
            else:
                if listt:
                    if listt.pop() != mapp[s[i]]:
                        return False
                else:
                    return False
        if len(listt) > 0:
            return False
        return True
            
