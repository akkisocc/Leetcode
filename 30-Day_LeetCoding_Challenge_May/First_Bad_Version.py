# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
import sys
"""
Input : [] -> ?
        [T,T,T,T] ->?
        [F,F,F] ->0

Algorithm:
1. left=0,right=n-1; mid
2. call isBadVersion(mid)
    -- True; store index and call on left
    -- False ; call on right


"""


class Solution:
    def helper(self,n,left,right,index):
        mid = left + (right-left)//2
        if left>right:
            return 
        output = isBadVersion(mid)
        if output==True:
            if mid<index[0]:
                index[0]=mid
            return self.helper(n,left,mid-1,index)
        if output==False:
            return self.helper(n,mid+1,right,index)
    
        
        
    def firstBadVersion(self, n):
        if n==0:
            return 1
        index =[sys.maxsize]
        self.helper(n,0,n,index)
        return index[0]
        
        
