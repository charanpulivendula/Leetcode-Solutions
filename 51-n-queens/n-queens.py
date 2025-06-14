from copy import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isValid(board,row,col):
            for x,y in board:
                if x == row:
                    return False
                if y == col:
                    return False
                if abs(row-x)==abs(col-y):
                    return False
            return True
        res = []
        def backtrack(board,level):
            if len(board)==n:
                temp_res = []
                for r,c in board:
                    temp_res.append("."*c+"Q"+"."*(n-c-1))
                res.append(temp_res)
                return
            for col in range(n):
                if isValid(board,level,col):
                    board.append((level,col))
                    backtrack(board,level+1)
                    board.remove((level,col))
            return
        backtrack([],0)
        return res

        
         




            


