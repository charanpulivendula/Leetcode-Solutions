class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in range(len(strs)):
            temp=strs[i]
            key="".join(sorted(strs[i]))
            if key in d:
                d[key].append(temp)
            else:
                d[key] = [temp]
        res=[]
        print(d)
        for i in d:
            res.append(d[i])
        return res