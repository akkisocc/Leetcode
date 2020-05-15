"""
Input: [1,-2,3,-2]
Input: [3,-1,2,-1]
Input : [-1] -> -1

Steps:
1. Case 1: If solution exists in straight array -> use Kadane
   Case 2 : If solution exists in circular part 
   -> then it is like a ring, where middle part is non contributing
2. How to find non-contributing elements for case -2 , basically apply Kadane to find min sum sub array
   Find total array sum , sum(A) - minsum = Case 2
3. return max(case1,case2)

Time Complexity - O(N)
Space Complexity - O(1)

"""


class Solution:
    def kadaneMax(self,a):
        n = len(a)
        curr=max_sum = a[0]
        for i in range(1,n):
            curr = max(a[i],curr+a[i])
            max_sum = max(curr,max_sum)
        return max_sum
    def kadaneMin(self,a):
        n = len(a)
        if n==1:
            return a[0]
        curr=min_sum = a[0]
        for i in range(1,n):
            curr= min(a[i],curr+a[i])
            min_sum = min(curr,min_sum)
        if sum(a) - min_sum == 0:
            return float(-inf)
        #print(sum(a) - min_sum)
        return sum(a) - min_sum
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        case1 = self.kadaneMax(A)
        case2 = self.kadaneMin(A)
        #print(case1)
        return max(case1,case2)
        
