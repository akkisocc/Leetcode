"""
5/2 = 2,rem = 1
2/2 = 1, rem = 0
1/2 = <1, rem = 1
4/2 = 2, rem = 0
2/2 = 1 , rem = 0
1/2 = <1 , rem = 1

Input : num = 0 -> 0 
        num = 1 -> 1

Steps :
1. res = ""
2. rem = n%2,temp/=2 res = rem+res ; 
3. repeat step 2 till temp>0


"""


class Solution:
    def findComplement(self, num: int) -> int:
        res =""
        temp = num
        if num==0:
            return 1
        while temp>0:
            rem = temp%2
            temp=temp//2
            res = str(rem)+res
        output=0;n = len(res)
        #print(res)
        for i in range(n-1):
            if res[i]=='0':
                output+=pow(2,n-i-1)
        
        if res[n-1]=='0':
            output+=1
        return output
    
        
