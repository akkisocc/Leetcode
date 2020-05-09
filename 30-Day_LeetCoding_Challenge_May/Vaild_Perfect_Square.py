import sys
sys.setrecursionlimit(10**9)
"""
Input: 14 -> 2*7 -> False
      36 -> 2*2*3*3 -> 2*3 -> True
      1 -> True
Steps:
1. Binary Search can be used
2. low = 0 ; high = n
3. find mid and calculate square
4. if square<n: search right half
5. if square>n:search left half
6. if square==n: return true
7. if low>high: return false


Time Complexity = O(logn)
Space Complexity = O(1) 
"""



class Solution:
    def binarySearch(self,n,low,high):
        mid = low + (high-low)//2
        
        if low>high:
            return False
        square = mid*mid
        if  square == n:
            return True
        if square<n:
            return self.binarySearch(n,mid+1,high)
        return self.binarySearch(n,low,mid-1)
        
    def isPerfectSquare(self, num: int) -> bool:
        return self.binarySearch(num,0,num)
       
            
        
