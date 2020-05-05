class Solution:
    def count(self,grid,visited,i,j,n,m):
        #print(i,'--',j)
        #print("n--",n,"m--",m)
        if i==n or j==m or j==-1 or i==-1:
            
            #print("first one")
            return 
        if i+1<n and j<m and grid[i+1][j]=='1' and visited[i+1][j]==False:
            #print("k")
            visited[i+1][j]=True
            self.count(grid,visited,i+1,j,n,m)
        if j+1<m and i<n and grid[i][j+1]=='1' and visited[i][j+1]==False:
            visited[i][j+1]=True
            #print("hello")
            self.count(grid,visited,i,j+1,n,m)
        if i-1>-1 and j<m and grid[i-1][j]=='1' and visited[i-1][j]==False:
            visited[i-1][j]=True
            self.count(grid,visited,i-1,j,n,m)
        if i<n and j-1>-1 and grid[i][j-1]=='1' and visited[i][j-1]==False:
            visited[i][j-1]=True
            self.count(grid,visited,i,j-1,n,m)
            
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid)==0:
            return 0
        n = len(grid); m = len(grid[0])
        #print(n,'->',m)
        visited = [[False for _ in range(m)] for __ in range(n)]
        res=0
        for i in range(n):
            for j in range(m):
                if visited[i][j]==False and grid[i][j]=='1':
                    visited[i][j]=True
                    self.count(grid,visited,i,j,n,m)
                    #print(visited)
                    #print("res-",res)
                    res+=1
        return res
        
