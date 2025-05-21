class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        twenty = 0
        for bill in bills:
            if bill == 5:
                five+=1
                continue
            elif bill == 10:
                if five==0:
                    return False
                five-=1
                ten+=1
            else:
                if five == 0:
                    return False
                elif ten == 0:
                    if five<3:
                        return False
                    else:
                        five-=3
                else:
                    ten-=1
                    five-=1
                twenty+=1
                
        return True

        