class Solution:
  def generateParenthesis(self, n):
    output = []
    def backtrack(string,res):
      if len(string)>2*n:
        return
      print(res)
      if res<0:
        return
      if len(string) == 2*n and res == 0:
        output.append(string)
      tempstring = string+"("
      backtrack(tempstring,res+1)
      tempstring = string + ")"
      backtrack(tempstring,res-1)
      return res

    backtrack("",0)
    return output