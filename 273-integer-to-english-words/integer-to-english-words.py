class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        dictionary = {1:"One",2:"Two", 3:"Three",4:"Four",5:"Five",6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 10:"Ten", 11:"Eleven", 12:"Twelve", 13: "Thirteen", 14: "Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen", 20:"Twenty", 30:"Thirty", 40:"Forty", 50: "Fifty", 60:"Sixty", 70:"Seventy", 80:"Eighty", 90:"Ninety",100:"Hundred", 1000:"Thousand",1000000:"Million", 1000000000:"Billion", 1000000000000:"Trillion"}
        values = [1000000000000,1000000000,1000000,1000,100,90,80,70,60,50,40,30,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
        temp = values[4:]

        def findval(number):
            tempres = []
            i = 0
            if number in dictionary:
                if number >= 100:
                    return ["One", dictionary[number]]
                return [dictionary[number]]
            while(number and i<len(temp)):
                count = number//temp[i]
                if count>0:
                    if number > 99:
                        tempres.append(dictionary[count])
                        tempres.append(dictionary[temp[i]])
                    else:
                        tempres.append(dictionary[temp[i]])
                    number%=temp[i]
                i+=1
            return tempres
        i = 0
        res = []
        while(num and i<len(values)):
            count = num//values[i]
            if count>0:
                if num>99:
                    tempres = findval(count)
                    res+=tempres
                res.append(dictionary[values[i]])
                num= num%values[i]
            i+=1

        return " ".join(res)
