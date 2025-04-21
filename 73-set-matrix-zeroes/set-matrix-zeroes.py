class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        flag=False
        m = len(matrix)
        n = len(matrix[0])
        isrow = False
        iscol = False
        for i in range(m):
            if matrix[i][0]==0:
                isrow = True
                break

        for i in range(n):
            if matrix[0][i]==0:
                iscol = True
                break


        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0


        # see if the first column needs to be set to zero as well        
        if isrow:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if iscol:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        return matrix
        
        