"""
Input = [1,1,2,3,3,4,4,8,8] -> mid=a[4], right = 4 , left = 4+1, so ans lies in left half
because of odd number
Input = Nothing mentioned about constraints. Assume unique element is always there, let's see
if this work 

Steps:
1. call binary search
2.1 if mid==0 -> return a[0]; if mid==n-1 -> return a[n-1]
2. if a[mid]!=a[mid+1] and a[mid]!=a[mid-1] --> return true
3. check if a[mid]==a[mid+1]: 
    check if mid -> elements at left side is not divisible by 2
    if True , call binary search on left
    else, call binary search on right
4. check if a[mid]==a[mid-1]:
    check if mid+1 -> elements at left side is not divisible by 2
    if True, call binary search on left
    else, call binary search on right
    
Time Complexity = O(log n)
Space Complexity = O(1)

"""




class Solution:
    def _find(self,a,left,right,n):
        mid = left+(right-left)//2
        if left>right:
            return -1
        if mid==0:
            return a[mid]
        if mid==n-1:
            return a[mid]
        if a[mid]!=a[mid+1] and a[mid]!=a[mid-1]:
            return a[mid]
        
        if a[mid]==a[mid+1]:
            if mid%2!=0:
                return self._find(a,left,mid-1,n)
            else:
                return self._find(a,mid+1,right,n)
        if a[mid]==a[mid-1]:
            if (mid+1)%2!=0:
                return self._find(a,left,mid-1,n)
            else:
                return self._find(a,mid+1,right,n)
        
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        return self._find(nums,0,n-1,n)
        
