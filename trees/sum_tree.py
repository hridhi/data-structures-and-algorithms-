class Solution:
    def toSumTree(self, root) :
        #code here
        def util(root):
            if not root:
                return 0
            val=root.data
            root.data =util(root.left)+util(root.right)
            return root.data+val 
        y=root
        util(y)
        return root
