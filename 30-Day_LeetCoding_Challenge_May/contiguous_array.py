from collections import defaultdict as dd
"""
[0,1,0] -> 2
[0] -> 0
[1] -> 1

0,1,1,1,1,0,1
Use the displacement approach

Steps:
1. Initialize a map with key= count , index as value
2. --count if 0, ++count if 1
3. If count exists in map then this means that this point has come before, store this to use if for max size
4. If count doesn't exits then put in map

"""


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        m1 = dd(lambda : None)
        n = len(nums);curr,_max = 0,0;count=0
        m1[count]=0
        for i in range(n):
            if nums[i]==0:
                count-=1
            else:
                count+=1
            if m1[count] == None:
                m1[count]=i+1
            else:
                curr = i-m1[count]+1
                _max = max(curr,_max)
            print(count)
        #print(m1)
                
        return _max
        
