"""
Input: s1 = "ab" s2 = "eidbaooo"

Steps:
1. store s1 frequency in m1
2. initialize i=0;j=0
3. while j< len(s2)
    -- if j-i+1=len(s1):
            if m1==m2:
                return true
            m2[i]--
            m2[j]++
            i--;
    -- if s2 is in m1:
            m2[s2]++
    -- if s2 not in m1:
            i=j+1
        j++


"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        _s1 = len(s1); _s2 = len(s2);m1={};m2={}
        for i in s1:
            if m1.get(i,0)==0:
                m1[i]=1
            else:
                m1[i]+=1
                
        i=0;j=0
        while j< _s2:
           
            
            if m1.get(s2[j],0)>0:
                if m2.get(s2[j],0)==0:
                    m2[s2[j]]=1
                else:
                    m2[s2[j]]+=1
                
            
            elif m1.get(s2[j],0)==0:
                m2.clear()
                i=j+1
                
            #print(m2)
            #print(i,"--j--",j)
            if j-i+1 == _s1:
                #print("he")
                if m1==m2:
                    return True
                m2[s2[i]]-=1
                i+=1
            j+=1
            
            
        return False
                
                
                
                
                
                
                
                
                
                
                
        o

