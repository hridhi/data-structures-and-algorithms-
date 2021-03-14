class Solution:
    def __init__(self):
        self.res=[]
    def deepestLeavesSum(self, root: TreeNode) -> int:
        depth=0
        ans=0
        self.printInorder(root,depth)
        self.res=sorted(self.res, key=itemgetter(1),reverse=True)
        req=self.res[0][1]
        for i in range(len(self.res)):
            if self.res[i][1]==req:
                ans+=self.res[i][0]
            else:
                break
        return ans
    def printInorder(self,root: TreeNode,depth: int): 
        if root:
            self.printInorder(root.left,depth+1)
            if root.left==None and root.right==None:
                self.res.append((root.val,depth)) 
            self.printInorder(root.right,depth+1)
