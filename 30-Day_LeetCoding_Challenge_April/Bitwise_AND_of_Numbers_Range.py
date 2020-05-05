import math
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while(n>m):
            n = n & n-1
        return m&n
        
        
        if m==0:
            return 0
     
        x=math.floor(math.log(n,2))
        x1 = 2**(x-1)
        x1 = int(x1)
      
     
        if x1<m:
            x1=m
        left = x1+1; right = n-1
        mid = left + (right-left)//2
        res1 = x1;res2=n
        #print(left,"->",right)
        while left<=right:
            res1 = res1 & left
            res2 = res2 & right
            #print(left,"--",right)
            left+=1
            right-=1
        
        return res1 & res2
        
        
