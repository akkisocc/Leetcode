# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root: TreeNode,_max):
        if root==None:
            return -1
        if root.left == None and root.right==None:
            return 0

        leftNode = 1+self.dfs(root.left,_max)
        rightNode = 1+self.dfs(root.right,_max)
        
        if _max[0]< leftNode+rightNode:
            _max[0]=leftNode+rightNode
        return diameter
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        _max = [0]
        x=self.dfs(root,_max)
        return _max[0]
