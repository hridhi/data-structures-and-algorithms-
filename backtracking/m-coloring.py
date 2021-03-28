def isSafe(graph,v,n,temp,color):
    for i in range(v):
        if (graph[n][i]==1 and color[i]==temp):
            return False
    return True
def check(graph,m,v,n,color):
    if(n==v):
        return True
    for i in range(1,m+1):
        if(isSafe(graph,v,n,i,color)):
            color[n]=i
            if(check(graph,m,v,n+1,color)):
                return True
            color[n]=0
    return False
def graphcoloring(graph,M,V):
    color=[0]*(V+1)
    return check(graph,M,V,0,color)
def main():
    for _ in range(int(input())):
        V=int(input())
        M=int(input())
        E=int(input())
        list=[int(x) for x in input().strip().split()]
        graph =[[0 for i in range(V)] for j in range(V)]
        cnt=0
        for i in range(E):
            graph[list[cnt]-1][list[cnt+1]-1]=1
            graph[list[cnt+1]-1][list[cnt]-1]=1
            cnt+=2
        if(graphcoloring(graph,M,V)==True):
            print(1,"/n")
        else:
            print(0,"/n")

if __name__ =='__main__':
    main()
