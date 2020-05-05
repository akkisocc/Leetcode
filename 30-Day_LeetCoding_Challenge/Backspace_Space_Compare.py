class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        res1 = "";res2=""
        n = len(s); m = len(t);countS=0;countT=0
        for i in range(n-1,-1,-1):
            if s[i] =='#' :
                countS+=1
            elif s[i] != '#' and countS==0:
                res1+=s[i]
            elif s[i] != '#' and countS!=0:
                countS-=1
                
        for j in range(m-1,-1,-1):
            if t[j] =='#' :
                countT+=1
            elif t[j] != '#' and countT==0:
                res2+=t[j]
            elif t[j] != '#' and countT!=0:
                countT-=1
        #print(res1,"--",res2)        
        return res1 == res2
            
        
