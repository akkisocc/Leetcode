"""
word1 = "horse", word2 = "ros" -> 3

Steps:
1. When char in both strings are same then don't do anything(i-1,j-1) . Consider the remaining one
2. When char are different
    -- Insert:- ab, bc --> b and c are not equal --> abc, bc --> now after insertion -> c and c are equal,
        we will reach to ab,b -> i, j-1
    -- Delete :- ab, bc --> a,bc-> bcoz we deleted from s1 --> i-1,j
    -- replace :- ab,bc --> ac,bc -> char are same --> a,b --> i-1,j-1
    Now take min(Insert,delete,replace) + 1, 1-> for the operation

Time Complexity :- O(m*n)
Space Complexity :- O(m*n)
"""



class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        n = len(s1); m = len(s2) 
        
        dp = [[ 0 for _ in range(m+1)] for __ in range(n+1)]
        #dp[n+1][m+1]
        
        for i in range(n+1):
            for j in range(m+1):
                if i==0:
                    dp[i][j]=j
                elif j==0:
                    dp[i][j]=i

                elif s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                
                else:
                    dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                    
        return dp[n][m]
                
                
                
                
                
                
                
                
                
                
        
