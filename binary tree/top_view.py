class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        res=[]
        dic={}
        mi=99999
        if not root :
            return 
        q=deque([(root,0)])
        while q:
            cur=q.popleft()
            if cur[1] not in dic:
                dic[cur[1]]=cur[0].data
                mi=min(mi,cur[1])
            if cur[0].left :
                q.append((cur[0].left,cur[1]-1))
            if cur[0].right :
                q.append((cur[0].right,cur[1]+1))
        while mi in dic:
            res.append(dic[mi])
            mi+=1
        return res 
        # code here
