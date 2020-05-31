"""
 A = [[0,2],[5,10],[13,23],[24,25]], 
 B = [[1,5],[8,12],[15,24],[25,26]]
 a_start = 0 , a_end = 2
 b_start = 1 , b_end = 5 --> 1,2 check if a_end > b_start -> (b_start,a_end)
 
 a_start = 0 , a_end = 2
 b_start = 3 , b_end = 5 --> b_start> a_end -- disjoint
 
 a_start = 1 , a_end = 5
 b_start = 0 , b_end = 2 --> (1,2) if a_start <b_end --> a_start,b_end
 
 Steps:
 1. initialize a_start,a_end,b_start,b_end
 2. while ?
 3. if a_start > b_start
    if a_start <= b_end : (a_start,b_end)    
4. if b_start>= a_start:
    if a_end >= b_start -- (b_start,a_end)
5. if a_start.next <= b_end
    (a_start.next,b_end)
6. if b_start.next <= a_end:
    b_start.next,a_end
    
    astart++,b_start++,a_end++,b_end++


"""

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        i = j = 0

        while i < len(A) and j < len(B):
            
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:
                ans.append([lo, hi])

            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return ans
        
        
        
        
