class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        i = 0
        j = 0
        memcache = {}
        def maxSum(i,j,iter):
            if (i,j) in memcache:
                return memcache[(i,j)]
            if iter>=len(triangle):
                memcache[(i,j)] = 0
                return memcache[(i,j)]
            memcache[(i,j)] = triangle[i][j]+min(maxSum(i+1,j,iter+1),maxSum(i+1,j+1,iter+1))
            return memcache[(i,j)]
        return maxSum(0,0,0)
                