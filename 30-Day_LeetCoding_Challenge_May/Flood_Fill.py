import sys
sys.setrecursionlimit(10**9)

"""
[[1,1,1],    2,2,2
 [1,1,0], -> 2,2,0
 [1,0,1]]    2,0,1
Input : [[1]],x ->[[x]]

Steps:
1. start from (sr,sc), and check if you can move in 4 directions or not
2. four directions , right = sr,sc+1, left = sr,sc-1, top= sr-1,sc, bottom = sr+1,sc
3. check before moving to four direction ,
    if sr>-1 and sr<n and sc>-1 and sc<m :
        if image[sr][sc]==image[_sr][_sc]:
            return True
    return False

Time Complexity = O(n*m)
Space Complexity = O(n*m)


"""



class Solution:
    def check(self,image,sr,sc,oldColor,newColor,n,m,dp):
        if sr>-1 and sr<n and sc>-1 and sc<m:
            if image[sr][sc]==oldColor and dp[sr][sc]==False:
                dp[sr][sc]=True
                return True
        return False
        
        
    def _flood(self,image,sr,sc,oldColor,newColor,n,m,dp):
        #print(image)
        #left
        if self.check(image,sr,sc-1,oldColor,newColor,n,m,dp):
            image[sr][sc-1]=newColor
            self._flood(image,sr,sc-1,oldColor,newColor,n,m,dp)
        #right
        if self.check(image,sr,sc+1,oldColor,newColor,n,m,dp):
            image[sr][sc+1]=newColor
            self._flood(image,sr,sc+1,oldColor,newColor,n,m,dp)
        #top
        if self.check(image,sr-1,sc,oldColor,newColor,n,m,dp):
            image[sr-1][sc]=newColor
            self._flood(image,sr-1,sc,oldColor,newColor,n,m,dp)
        #bottom
        if self.check(image,sr+1,sc,oldColor,newColor,n,m,dp):
            image[sr+1][sc]=newColor
            self._flood(image,sr+1,sc,oldColor,newColor,n,m,dp)
        
        
        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        n=len(image);m=len(image[0])
        oldColor = image[sr][sc]
        dp = [[False]*m for _ in range(n)]
        image[sr][sc]=newColor
        self._flood(image,sr,sc,oldColor,newColor,n,m,dp)
        return image
        
        
