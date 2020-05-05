"""
Input : j = "" s = "abc" -> return 0
        j = "abc" s ="" -> return 0
        
Steps:
1. store s frequency in map
2. for each s find if it exists in map
    if True:
        res+=1
    
"""



class Solution:
    def numJewelsInStones(self, j: str, s: str) -> int:
        if len(s)==0 or len(j)==0:
            return 0
        m1 = {}
        for i in j:
            if m1.get(i,0) == 0:
                m1[i]=1
            else:
                m1[i]+=1
        res = 0
        for c in s:
            if m1.get(c,0)!=0:
                res+=1
                
        
        
        return res
        
