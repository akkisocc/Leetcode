"""
Input : s="" -> -1 , s = aabb -> -1

Steps:
1. create a map to store frequency
2. iterate over map and print first key with value as 1

"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        m1 = {};char="";n=len(s)
        if n==0:
            return -1
        
        for i in s:
            if m1.get(i,0)==0:
                m1[i]=1
            else:
                m1[i]+=1
                
        for key,val in m1.items():
            if val==1:
                char=key
                break
        for i in range(n):
            if s[i]==char:
                return i
                
        
        return -1
