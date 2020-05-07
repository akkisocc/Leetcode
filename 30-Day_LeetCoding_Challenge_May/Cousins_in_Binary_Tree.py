# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Input : if [1,2] -> False

Steps :
1. Initialze two list , l1=[None,None] and l2=[None,None]
2. call dfs on root
3. if x == root.val , store parent and depth in l1
4. if y == root.val , store parent and depth in l2
5. if l1[1]!=l2[1] and l1[0]==l2[0], return True

Time Complexity : O(N+E)
Space Complexity : O(1)



"""
class Solution:
    def _cousin(self,root,x,y,l1,l2,dep):
        if root==None:
            return
        self._cousin(root.left,x,y,l1,l2,dep+1)
        if l1[0]!=None and l1[1]==None:
            l1[1]=root.val
        if l2[0]!=None and l2[1]==None:
            l2[1]=root.val    
        self._cousin(root.right,x,y,l1,l2,dep+1)
        if l1[0]!=None and l1[1]==None:
            l1[1]=root.val
        if l2[0]!=None and l2[1]==None:
            l2[1]=root.val
        if x==root.val:
            l1[0]=dep
        if y==root.val:
            l2[0]=dep
    
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        l1 =[None,None]
        l2 = [None,None]
        self._cousin(root,x,y,l1,l2,0)
        #print(l1,"--",l2)
        if l1[0]==l2[0] and l1[1]!=l2[1]:
            return True
        return False

