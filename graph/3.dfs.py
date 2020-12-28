'''
g : adjacency list of graph
N : number of vertices

return a list containing the DFS traversal of the given graph
'''
def dfs_trial(g,i,visited,arr):
    if visited[i]==True:
        return
    else:
        arr.append(i)
        visited[i]=True
        for u in g[i] :
            if not visited[u]:
                dfs_trial(g,u,visited,arr)
def dfs(g,N):
    visited=[False]*N
    arr=[]
    dfs_trial(g,0,visited,arr)
    return arr 
    
