import sys
sys.setrecursionlimit(10**8)
"""
Input : [8,5,1,7,10,12]
        [8] --> 8

Steps:
1. root = a[0]
2. Iterate over list and find larger element larger than root, split here
3. root.left = [:pos]; root.right = [pos:]

"""


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
            return TreeNode(preorder[0])
            
        root = TreeNode(preorder[0])
        lt,rt=[],[]
        for i in range(1,len(preorder)):
            if root.val >preorder[i]:
                lt.append(preorder[i])
            else:
                rt.append(preorder[i])
        
        root.left = self.build(lt)
        root.right = self.build(rt)
        
                
                
        
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return self.build(preorder)
        
