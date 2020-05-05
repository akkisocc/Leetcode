import sys
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid)==0:
            return 0
        n = len(grid);m = len(grid[0])
        dp = [[sys.maxsize for _ in range(m)] for __ in range(n)]
        dp[0][0]=grid[0][0]
        for i in range(n):
            for j in range(m):
                if i+1<n:
                    dp[i+1][j] = min(dp[i+1][j],dp[i][j]+grid[i+1][j])
                if j+1<m:
                    dp[i][j+1] = min(dp[i][j+1],dp[i][j]+grid[i][j+1])
                    
        return dp[n-1][m-1]
        
