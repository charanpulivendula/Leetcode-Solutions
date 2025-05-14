class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        
        def nextsmaller(arr):
            res = [n] * n
            stack = []
            for i, elem in enumerate(arr):
                while stack and arr[stack[-1]] >= elem:
                    res[stack.pop()] = i
                stack.append(i)
            return res

        def previoussmaller(arr):
            res = [-1] * n
            stack = []
            for i in range(n - 1, -1, -1):
                while stack and arr[stack[-1]] > arr[i]:
                    res[stack.pop()] = i
                stack.append(i)
            return res

        nse_arr = nextsmaller(arr)
        pse_arr = previoussmaller(arr)
        
        mod = 10**9 + 7
        result = 0
        for i in range(n):
            result = (result + (nse_arr[i] - i) * (i - pse_arr[i]) * arr[i]) % mod
        return result
