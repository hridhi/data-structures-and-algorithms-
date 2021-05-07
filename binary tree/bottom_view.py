def bottomView(root):
    
    # code here
    if not root:
        return 
    dic={}
    q=[]
    mi=99999
    res=[]
    q.append((root,0))
    while(q):
        cur=q[0]
        q.pop(0)
        hd=cur[1]
        mi=min(mi,hd)
        dic[hd]=cur[0].data
        if cur[0].left:
            q.append((cur[0].left,hd-1))
        if cur[0].right:
            q.append((cur[0].right,hd+1))
    while mi in dic:
        res.append(dic[mi])
        mi+=1
    return res
