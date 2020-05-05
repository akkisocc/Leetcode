class Solution:
    def isHappy(self, n: int) -> bool:
        res = []
        temp = n
        while temp not in res:
            res.append(temp)
            s=0
            while temp>0:
                digit = temp%10
                s+=digit**2
                temp=temp//10
            temp = s
            
            if temp==1:
                return True
        
        return False
        
