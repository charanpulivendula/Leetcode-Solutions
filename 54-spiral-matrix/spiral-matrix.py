class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_f = 0
        row_l = len(matrix)-1
        col_f = 0
        col_l = len(matrix[0])-1
        reqcounter  = len(matrix)*len(matrix[0])
        counter  = 0
        res = []
        while(row_f<=row_l and col_f<=col_l):
            for i in range(col_f,col_l+1):
                res.append(matrix[row_f][i])
            row_f+=1
            for i in range(row_f,row_l+1):
                res.append(matrix[i][col_l])
            col_l-=1
            # print(col_l,col_f)
            if row_f<=row_l:
                for i in range(col_l,col_f-1,-1):
                    res.append(matrix[row_l][i])
                row_l-=1
            if col_f<=col_l:
                for i in range(row_l,row_f-1,-1):
                    res.append(matrix[i][col_f])
                col_f+=1
            
        return res
