from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        string_list = list(map(lambda x : str(x),nums))
        def compare(a,b):
            if a+b > b+a:
                return -1
            else:
                return 1
        res = "".join(sorted(string_list,key = cmp_to_key(compare)))
        if res[0]=='0':
            return '0'
        else:
            return res