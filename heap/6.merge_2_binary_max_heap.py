import heapq
t=int(input())
while t>0:
    #taking inputs 
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    # merge the arrays 
    a=a+b
    # now find the max heap 
    heapq._heapify_max(a)
    print(a)
    t=t-1
