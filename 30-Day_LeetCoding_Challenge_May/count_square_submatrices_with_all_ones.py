class Solution:
    def square(self,m,i,j,rows,cols,dp):
        #print(i,"--",j)
        #print(rows,"--",cols)
        if i>rows or j>cols:
            #print("h")
            return 0
        if m[i][j]==0:
            #print("m")
            return 0
        l=0;b=0;c=0
        if dp[i][j]!=None:
            return dp[i][j]
        if m[i][j]==1:
            #print("q")
            l = 1+self.square(m,i+1,j,rows,cols,dp)
            b = 1+self.square(m,i,j+1,rows,cols,dp)
            c = 1+self.square(m,i+1,j+1,rows,cols,dp)
        
        #print("out")
        x = min(l,b,c)
        #area = x*x
        dp[i][j]=x
        #print(dp)
        #print(x)
        return x
    
    
    def countSquares(self, m: List[List[int]]) -> int:
        rows = len(m)
        cols=0
        if rows>0:
            cols = len(m[0])
        dp = [[None for i in range(cols)]for j in range(rows)]
        #print(dp)
        curr = None; res = []
       
        for i in range(rows):
            for j in range(cols):
                curr=self.square(m,i,j,rows-1,cols-1,dp)
                res.append(curr)
        
        return sum(res)
        
