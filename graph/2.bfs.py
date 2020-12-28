from collections import deque
'''
*  g[]: adj list of the graph
*  N : number of vertices
'''
def bfs(g,N):
    # code here
    res=[]
    q= deque()
    q.append(0)
    visited=[False]*N
    visited[0]=True
    while q :
        sz=len(q)
        for i in range(sz):
            curr=q.popleft()
            res.append(curr)
            temp=g[curr]
            for x in temp:
                if not visited[x]:
                    visited[x]=True
                    q.append(x)
        
    return res 
