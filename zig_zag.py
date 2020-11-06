import queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        
        q  = queue.Queue()
        q.put(root)
        
        res=[] 
        
        while not q.empty():   
            a=[]
            size = q.qsize()    
            
            while size!=0:
                curr = q.get()
                a.append(curr.val)
                
                if curr.left:
                    q.put(curr.left)
                if curr.right:
                    q.put(curr.right)
                
                size-=1
            
            if len(a)!=0:
                res.append(a)
                
        # For Alternation
        
        for i in range(0,len(res)):
            if i%2!=0:
                res[i].reverse()
                
        return res
