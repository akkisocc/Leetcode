"""
Input : [[1,1],[0,0],[-1,-1]] slope = -1/-1 = 1, slope = 1/1 = 1 , -->return True

Steps:
1. Calculate slope for two points, store slope
2. For new iteration, repeat step 1 but store prevSlope = slope , if prevSlope == slope, repeat step1
3. if prevSlope != slope , return False 
4. Else list is exhausted return True

Time Complexity = O(N)
Space Complexity = O(1)

"""


class Solution:
    def checkStraightLine(self, a: List[List[int]]) -> bool:
        n = len(a)
        slope = None;prevSlope=None
        for i in range(n-1):
            if (a[i+1][0] - a[i][0]) == 0:
                slope = 0
            else:
                slope = (a[i+1][1] - a[i][1]) / (a[i+1][0] - a[i][0])
            if prevSlope!=None and prevSlope != slope:
                return False
            prevSlope = slope
            
        return True
                
        
        
