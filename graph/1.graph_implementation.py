# implemented graph using a dictionary in python 
from collections import defaultdict

class graph:
    def __init__(self,vertices_num):
        self.v=vertices_num
        self.g=defaultdict(list)
        
    def addEdge(self,u,v):
        self.g[u].append(v)
        #if undirected then self.g[v].append(u)
        
    def print_graph(self): 
        for i in range(self.v): 
            print("Adjacency list of vertex {}\n head".format(i), end="") 
            temp = self.g[i] 
            for u in temp: 
                print(" -> {}".format(u), end="") 
            print(" \n")
            
# main program 
g = graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)



g.print_graph()
