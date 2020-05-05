class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n==0 :
            return False
        if n==1:
            return True
        step=0
        for i in range(n):
            if i>step:
                return False
            if i+nums[i]>=n-1:
                return True
            if i+nums[i]>step:
                step=i+nums[i]
        
        """dp = [False]*n
        
        dp[0]=True
        for i in range(n):
            if dp[i]==True:
                j=i+1
                for _ in range(nums[i]):
                    if j<n:
                        dp[j]=True
                    if dp[n-1]==True:
                        return True
                    j+=1
            else:
                return False
           # print(dp)
        return dp[n-1]
        """

        

