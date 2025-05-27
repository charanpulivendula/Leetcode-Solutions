class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        visited=set()

        def isvalid(i,j):
            return 0<=i<m and 0<=j<n and board[i][j]=="O" and (i,j) not in visited

        def dfs(i,j):
            if not isvalid(i,j):
                return
            visited.add((i,j))
            board[i][j]="N"
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i-1,j)

        for i in range(m):
            for j in range(n):
                if i==0 or j == 0 or i == m-1 or j == n-1:
                    if board[i][j] == 'O':
                        dfs(i,j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "N":
                    board[i][j] = "O"
        return board


        
    
