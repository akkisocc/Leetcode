
"""
Input : [[1,1]] -> -1

Steps:
1. Initialize set s to store vertices going to other vertices (v1->v2), s=(v1)
2. Initialize map m1 to store frequency of ending vertices (Eg. v2)
3. vertices in s are not the ans, if v2 is in s then m1[v2]=0
4. find m1[x] == n-1, if exits return x else -1


Time Complexity : O(n)
Space Complexity : O(n)

"""



class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        s = set()
        n = len(trust)
        m1 = {}
        if N==1 and n==0:
            return 1
        for i in range(n):
            s.add(trust[i][0])
            if trust[i][1] in s:
                m1[trust[i][1]]=0
            else:
                if m1.get(trust[i][1],0)==0:
                    m1[trust[i][1]]=1
                else:
                    m1[trust[i][1]]+=1
       
        for key,val in m1.items():
            if val == N-1 and key not in s:
                return key
        
        return -1
        
