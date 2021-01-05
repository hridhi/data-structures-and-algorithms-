def isBipartite(self,src):
    colArr=[-1]*self.v
    colArr[src]=1
    queue=[]
    queue.append(src)
    while(queue):
      u=queue.pop()
      if self.graph[u][u]==1: # if self loop return false 
        return False
      for v in range(self.v):
        if self.graph[u][v]==1 and colArr[v]==-1:
          if colArr[u]==1:
            colArr[v]=0
          elif colArr[u]==0:
            colArr[v]=1
          queue.append(v)
        elif self.graph[u][v]==1 and colArr[v]==colArr[u]:
          return False

    return True
