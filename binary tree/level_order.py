def levelOrder( root ):
    # Code here
    q=[]
    arr=[]
    q.append(root)
    while (q):
        s=q[0]
        arr.append(s.data)
        q.pop(0)
        if s.left != None:
            q.append(s.left)
        if s.right !=None:
            q.append(s.right)
    return arr 
