def isHeap(root):
    #Code Here
    #it is a max heap 
    r=root.data
    if root.left==None and root.right==None:
        return True 
    elif root.left!=None and root.right==None:
        temp=root.left.data
        if r>=temp:
            return isHeap(root.left)
        else:
            return False
    elif root.left==None and root.right!=None:
        temp=root.right.data
        if r>=temp:
            return isHeap(root.right)
        else:
            return False
    else:
        if r>=max(root.right.data,root.left.data):
            return isHeap(root.right) and isHeap(root.left)
        else:
            return False
