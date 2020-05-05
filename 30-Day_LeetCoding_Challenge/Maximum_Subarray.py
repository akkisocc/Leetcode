class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a = [0]*len(nums)
        if len(nums)==1:
            return nums[0]
      
        a[0] = nums[0]
        for i in range(1,len(nums)):
            if a[i-1] + nums[i] > nums[i]:
                a[i] = a[i-1] + nums[i]
            else:
                a[i] = nums[i]
        return max(a)
        
