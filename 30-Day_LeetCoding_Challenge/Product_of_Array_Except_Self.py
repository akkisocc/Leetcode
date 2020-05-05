class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        output = [1]*n
        prefix = [0]*n
        suffix = [0]*n
        prefix[0]=nums[0]
        for i in range(1,n):
            prefix[i] =prefix[i-1]*nums[i]
        suffix[n-1]=nums[n-1]
        for j in range(n-2,-1,-1):
            suffix[j]=suffix[j+1]*nums[j]
            
        for i in range(n):
            if i-1>=0:
                output[i]*=prefix[i-1]
            if i+1<n:
                output[i]*=suffix[i+1]
                
        return output
