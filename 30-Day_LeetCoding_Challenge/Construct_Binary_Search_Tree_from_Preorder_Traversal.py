# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def build(self,preorder):
        #print(preorder)
        if len(preorder)==0:
            return None
        if len(preorder)==1:
            root = TreeNode(preorder[0])
            return root
        
        x = preorder[0];lt=[];rt=[]
        for i in preorder[1:]:
            if i<x:
                lt.append(i)
            else:
                rt.append(i)
        root = TreeNode(x)
        root.left = self.build(lt)
        root.right = self.build(rt)
        #print(root)
        return root
                
                
        
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return self.build(preorder)
        
