from collections import defaultdict as dd
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m1 = dd(list)
        for i in strs:
            temp=''.join(sorted(i))
            m1[temp].append(i)
        res =[]
        for key,value in m1.items():
            res.append(value)
            
        return res
