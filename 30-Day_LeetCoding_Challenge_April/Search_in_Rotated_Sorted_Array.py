class Solution:
    def _search(self,a,target,left,right):
        n = len(a)
        mid = left + (right-left)//2
        #print(mid)
        if left> right:
            return -1

        if a[mid]==target:
            return mid
        output=None
        if a[mid]>target  :
            output=self._search(a,target,left,mid-1)
            if output!=-1:
                return output
        if a[mid]<target  :
            output=self._search(a,target,mid+1,right)
            if output!=-1:
                return output

        output = self._search(a,target,mid+1,right)
        if output !=-1:
            return output
        output = self._search(a,target,left,mid-1)
        if output !=-1:
            return output
        
        return -1
    
        
    
        
    def search(self, a: List[int], target: int) -> int:
        n = len(a)
        left = 0
        right = n-1
        if n==1:
            return 0 if a[0]==target else -1
        return self._search(a,target,left,right)
        
        
