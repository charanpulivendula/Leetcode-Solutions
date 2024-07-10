class Solution:
  def validateStackSequences(self, pushed, popped):
    stack = []
    for i in range(len(pushed)):
      stack.append(pushed[i])
      while(popped and stack and stack[-1]==popped[0]):
        stack.pop()
        popped = popped[1:]
    if not stack:
      return True
    
    return False