class Solution:
  def numRabbits(self, answers):
    hash = {}
    for rabbit in answers:
      if rabbit in hash:
        hash[rabbit]+=1
      else:
        hash[rabbit] = 1
    count = 0
    for key,val in hash.items():
      temp = key+1
      count+= math.ceil(val/(temp))*temp
    return count