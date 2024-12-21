class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # checking row
        m = 9
        n = 9
        rowset = set()
        colset = set()
        validset = set()
        def valid(i,j):
            validset.clear()
            for x in range(i,i+3):
                for y in range(j,j+3):
                    if board[x][y] != ".":
                        if board[x][y] in validset:
                            return False
                        validset.add(board[x][y])
            
            return True

        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    if board[i][j] in rowset:
                        return False
                    rowset.add(board[i][j])
                if board[j][i]!=".":
                    if board[j][i] in colset:
                        return False
                    colset.add(board[j][i])
            # print(rowset)
            rowset.clear()
            colset.clear()
        
        # blockrow = 0
        # blockcol = 0
        for i in range(0,7,3):
            for j in range(0,7,3):
                if not valid(i,j):
                    return False
        return True
                
        