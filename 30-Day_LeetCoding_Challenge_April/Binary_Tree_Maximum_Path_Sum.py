import sys
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPath(self,root,_max):
        if root==None:
            return 0
        
        
        #print(root.val)
        opt1 = self.maxPath(root.left,_max)
        opt2 = self.maxPath(root.right,_max)
        
        #print(opt1,"--",opt2)
        temp =  max(max(opt1,opt2)+root.val,root.val)
        output = max(opt1+opt2+root.val,temp)
        #print("root.val--",root.val)
        #print(output)
        _max[0]=max(_max[0],output)
        
        return temp
      
    
    def maxPathSum(self, root: TreeNode) -> int:
        _max =[]
        _max.append(float('-inf'))
        self.maxPath(root,_max)
        return _max[0]
       
       
        
        
