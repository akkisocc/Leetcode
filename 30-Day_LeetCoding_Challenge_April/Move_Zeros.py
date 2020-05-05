class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i,j = 0,0
        n = len(nums)
        while i <n and j <n:
            if nums[j]!=0:
                nums[i],nums[j] = nums[j], nums[i]
                i+=1
            j+=1
                
     
                
