from collections import deque as dq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        a =dq(stones)
        while len(a)>1:
            a=dq(sorted(a,reverse=True))
            if a[0]==a[1]:
                a.popleft()
                a.popleft()
            else:
                a[0] = a[0] - a[1]
                del a[1]
                
        if len(a)==1:
            return a[0]
        
        return 0
                
        
