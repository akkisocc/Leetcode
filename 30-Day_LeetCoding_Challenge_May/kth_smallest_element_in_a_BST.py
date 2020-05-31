"""
  3
  / \   and k =1 ---> ans =1
 1   4  and k=3 ---> ans =3
  \
   2
root= Null, k =1 return ?
1,2,3 and k = 10 return ?
Steps:
1. Do inorder traversal of BST store it in list.
2. print kth element



"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self,root,a):
        if root == None:
            return
        self.traverse(root.left,a)
        a.append(root.val)
        self.traverse(root.right,a)
        
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        a = []
        self.traverse(root,a)
        return a[k-1]
        
