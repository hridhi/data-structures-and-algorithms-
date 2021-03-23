def derangements(n):
    #dynamic programming table 
    d=[0 for i in range(n+1)]
    #base casses 
    d[1]=0
    d[2]=1
    for i in range(3,n+1):
        d[i]=(i-1)*(d[i-1]+d[i-2])
    return d[n]
#Driver code 
for _ in range(int(input())):
    n=int(input())
    print(derangements(n))
