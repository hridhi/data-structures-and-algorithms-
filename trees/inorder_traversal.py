# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.inorderTraversalHelper( root, res )
        return res
    
     def inorderTraversalHelper(self, node, res):
        if node:
            if node.left:
                self.inorderTraversalHelper(node.left, res)
                
            res.append(node.val)
            
            if node.right:
                self.inorderTraversalHelper(node.right, res)
    
