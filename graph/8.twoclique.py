def checkTwoCliques(G):
    global V
    # finding complement of the graph
    GC = [[None] * V for i in range(V)] 
    for i in range(V): 
        for j in range(V): 
            GC[i][j] = not G[i][j] if i != j else 0
    return isBipartite(GC)
