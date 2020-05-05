#[7,1,5,3,6,4]
class Solution:
    def maxProfit(self, a: List[int]) -> int:
        if len(a)==0:
            return 0
        n = len(a)
        dp = [0]*n
        for i in range(n-1,-1,-1):
            if i+1<n:
                j=i+1
                if a[i]<a[j]:
                    dp[i]=dp[i+1]+a[j]-a[i]
                else:
                    dp[i]=dp[i+1]

        return dp[0]

        
