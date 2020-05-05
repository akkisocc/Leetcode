class Solution:
    def singleNumber(self, a: List[int]) -> int:
        res=0
        for i in range(len(a)):
            res^=a[i]
            
        return res
            
