class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def findrow():
            l = 0
            r = len(matrix)-1
            while(l<=r):
                mid = (l+r)//2
                if matrix[mid][0]<=target<=matrix[mid][-1]:
                    return mid
                elif matrix[mid][0]>target:
                    r = mid-1
                elif matrix[mid][-1]<target:
                    l = mid+1
            return l
        row = findrow()
        if row<0 or row>=len(matrix):
            return False
        l = 0
        r = len(matrix[row])
        while(l<=r):
            mid =(l+r)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid]>target:
                r = mid-1
            else:
                l = mid+1
        
        return False