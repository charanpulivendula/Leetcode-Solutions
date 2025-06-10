class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1
        steps = 0
        for _ in range(n):
            steps = a+b
            a = b
            b = steps
        return b