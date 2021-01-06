import heapq
def minCost(a,n) :
    cost=[]
    res=0
    heapq.heapify(a)
    while len(a)>1 :
        x=heapq.heappop(a)
        y=heapq.heappop(a)
        res=x+y
        cost.append(res)
        heapq.heappush(a,res)
    res=0
    for i in cost:
        res+=i
    return res

