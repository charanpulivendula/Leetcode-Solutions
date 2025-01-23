class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(remaining,combination,start):

            if remaining == 0:
                result.append(list(combination)) #make a deep copy
                return
            
            if remaining < 0:
                return
            
            for i in range(start,len(candidates)):
                combination.append(candidates[i])
                backtrack(remaining-candidates[i],combination,i) # not i+1 bacause we can reuse elements
                combination.pop()
        
        backtrack(target,[],0)
        return result