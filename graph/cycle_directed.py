def iscyclen(self,i,visited):
        visited[i]=True
        for u in self.g[i]:
            if not visited[u]:
                if self.iscyclen(u,visited):
                    return True
            elif visited[u]:
                return True
    def iscycle(self):
        visited=[False]*self.v
        for i in range(self.v):
            if visited[i]==False:
                if self.iscyclen(i,visited):
                    return True
        return False
    def iscycle_bfs(self):
        # computing the in - degree
        in_degree=[0]*self.v
        for i in range(self.v):
            for j in self.g[i]:
                in_degree[i]+=1
                
        # enque all vertices with 0 indegree
        queue=[]
        for i in range(len(in_degree)):
            if in_degree==0:
                queue.append(i)
                
        # One by one dequeue vertices from queue and enqueue 
    # adjacents if indegree of adjacent becomes 0 
        cnt=0
        while(queue):
            n=queue.pop(0)
            for v in graph[n]:
                in_degree[v]-=1
                if in_degree[v]==0:
                    queue.append(v)
            cnt+=1
            
        #If count of visited nodes is not equal
            #to the number of nodes in the graph has cycle, otherwise not.
        if cnt==self.v:
            return False
        else:
            return True
