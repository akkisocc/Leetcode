from collections import defaultdict as dd
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = dd(int)
        res[0]=1;total=0;count=0
        for i in range(n):
            total+=nums[i]
            if res[total-k]!=0:
                count+=res[total-k]
                
            res[total]+=1
            #print("total--",total)
            #print(res)
            #print("k-total ",k-total)
        return count
            
        
