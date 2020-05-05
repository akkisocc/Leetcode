"""
Input :- "" , "abc" -> True
         "abc" , "" -> False

Steps:
1. store magzine frequency in map
2. check each i in ransom:
    if contains: i++,decrement map value by 1
    else False
    
    return True

"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        n=len(ransomNote);m = len(magazine)
        if n==0 :
            return True
        if m!=0 and n==0:
            return False
        m1 = {}
        for i in magazine:
            if m1.get(i,0)==0:
                m1[i]=1
            else:
                m1[i]+=1
        #print(m1)
        for i in ransomNote:
            if m1.get(i,0)!=0:
                m1[i]-=1
            else:
                return False
            
        return True
                
        
