class Solution:
    def reverseBits(self, n: int) -> int:
        rev_string = bin(n)[2:][::-1]
        rev_string+="0"*(32-len(rev_string))
        return int(rev_string,2)