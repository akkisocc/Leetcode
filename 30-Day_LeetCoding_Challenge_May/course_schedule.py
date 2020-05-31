from collections import defaultdict as dd
"""
Just detect a cycle in graph if true return false if false return true

Steps:
1. Main three sets
    to_process = contains all vertices which we need to process
    visited = contains all the vertices which are visited
    processed = contains all vertices which have all its children processed like leaf vertice or end vertices
2. put all the vertices to to_process set
3. start from one vertice from to_process set
4. run dfs and mark that vertice which is visited in visited set
5. when no child is left to process for that particular vertice , move to visited ->  processed
6. At any point if the vertice which we are currently processing exists in visited set then there is cycle
7. Else after every vertice is processed in to_process set return no cycle
"""

class Solution:
    def dfs(self,g,to_process,visited,processed,src):
        visited.add(src)
        #print(visited)
        for neighbour in g[src]:
            if neighbour in processed:
                continue
            if neighbour not in visited:
                res=self.dfs(g,to_process,visited,processed,neighbour)
                if res==True:
                    return True
            else:
                #print("h")
                return True
        visited.remove(src)
        processed.add(src)
        #print("after--",visited)
        return False
            
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        to_process = set()
        visited = set()
        processed = set()
        edges = len(prerequisites)
        g = dd(list)
        for i in range(numCourses):
            to_process.add(i)
        for e in prerequisites:
            g[e[1]].append(e[0])
        #print(g)
        for i in to_process:
            if self.dfs(g,to_process,visited,processed,i) == True:
                return False
        
        return True
        
        
