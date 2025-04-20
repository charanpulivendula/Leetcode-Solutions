class Solution:
    def reverse(self, x: int) -> int:
        rev_no = str(x)[::-1]
        if rev_no[-1]=="-":
            rev_no =  -1*int(rev_no[:-1])
        else:
            rev_no = int(rev_no)
        
        if -2**31 <=rev_no<=2**31-1:
            return rev_no
        else:
            return 0
        