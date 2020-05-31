class Solution:
    
    def maxUncrossedLines(self, a: List[int], b: List[int]) -> int:
        n = len(a); m = len(b)
        # dp[n][m]
        dp = [ [0 for j in range(m+1)]for i in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if a[i-1]==b[j-1]:
                    dp[i][j]= 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[n][m]
        
        
