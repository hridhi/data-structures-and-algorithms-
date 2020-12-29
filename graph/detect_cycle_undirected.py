# using dfs
def detectcycle(graph,visited,i,parent):
    visited[i]=True
    for j in graph[i]:
        if visited==False:
            if detectcycle(graph,visited,j,i):
                return True
            elif parent!=j:
                return True
    return False
def isCyclic(g,n):
    '''
    :param g: given adjacency list representation of graph
    :param n: no of nodes in graph
    :return:  boolean (whether a cycle exits or not)
    '''
    # code here
    #dfs solution 
    visited=[False]*n
    for i in range(n):
        if visited[i]==False:
            if detectcycle(g,visited,i,-1):
                return 1
    return 0 
