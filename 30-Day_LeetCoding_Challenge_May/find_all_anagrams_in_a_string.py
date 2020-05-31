from collections import Counter
from copy import copy
"""
Input = "" ,"a" -> ?
        "a" , "abc" -> ?
        
Steps:
1. store freq of p in m1
2. initilize i=0;j=0
3. m2 = m1 
4. if m2[s[j]] > 0: m2[s[j]]-=1, if m2[s[j]]==0: del m2[s[j]]; j+=1
5. if m1[s[j]] == 0: j+=1,i=j m2 = m1
6. j-i+1 == len(p) and len(m2)==0: res.append(i) ;  m2[s[i]]-=1 , i+=1

"""

#s: "abab" p: "ab"
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        cnt_p = Counter(p); n = len(s); m = len(p); res = []
        for i in range(n-m+1):
            if i == 0: cnt_s = Counter(s[:m])
            else:
                prev = s[i-1]; curr = s[i+m-1]
                cnt_s[prev] -= 1; cnt_s[curr] += 1
                if cnt_s[prev] == 0: del cnt_s[prev]
            if cnt_s == cnt_p: res.append(i)
        return res        
                
            
                
            
            
            
            
            
            
            
            
            
            
        
