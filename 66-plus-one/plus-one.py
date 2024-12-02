class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]!=9:
            digits [-1]+=1
            return digits
        else:
            carry = 1
            digits[-1]=0
            i = len(digits)-2
            while(carry and i>=0):
                sumer = carry+digits[i]
                digits[i] = sumer%10
                carry = sumer // 10
                i-=1
            if carry:
                return [1]+digits
            return digits

        