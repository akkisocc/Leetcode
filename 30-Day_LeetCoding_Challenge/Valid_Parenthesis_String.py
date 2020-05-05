class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        first, second = 0,0
        for i in range(n):
            if s[i] == '(':
                first+=1
            elif s[i] == '*':
                first+=1
            else:
                first-=1
            
            if s[n-1-i] == '*':
                second+=1
            elif s[n-1-i] == ')':
                second+=1
            else:
                second-=1
            
            if first<0 or second<0:
                return False
            
            
        return True
