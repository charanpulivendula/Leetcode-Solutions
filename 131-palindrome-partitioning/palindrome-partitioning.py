class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(s):
            return s==s[::-1]

        def recursion(arr,index):
            if index==len(s):
                res.append(list(arr))
                return True
            if index>len(s):
                return False
            for j in range(index,len(s)):
                if isPalindrome(s[index:j+1]):
                    arr.append(s[index:j+1])
                    recursion(arr,j+1)
                    arr.pop()
        recursion([],0)
        return res
            
    