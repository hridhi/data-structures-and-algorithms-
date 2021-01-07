def balanceHeaps():
    if abs(len(min_heap)-len(max_heap)) <= 1:
        return 
    if len(min_heap)>len(max_heap): # min_heap has more data
        value_top = heapq.heappop(min_heap)
        heapq.heappush(max_heap,-1*value_top) # value inserted in max heap
    else:
        value_top = -1* heapq.heappop(max_heap) 
        heapq.heappush(min_heap,value_top) 
    return
def getMedian():
    if len(max_heap)>len(min_heap):
        value = heapq.heappop(max_heap)
        heapq.heappush(max_heap,value) 
        return (-1*value)
    elif len(min_heap)>len(max_heap):
        value = heapq.heappop(min_heap)
        heapq.heappush(min_heap,value)
        return value
    else:
        val_min = heapq.heappop(min_heap)
        val_max = -1*heapq.heappop(max_heap)
        heapq.heappush(min_heap,val_min)
        heapq.heappush(max_heap,-1*val_max)
        return ((val_max+val_min)//2)
def insertHeaps(x):
    least_upperhalf = heapq.heappop(min_heap) if len(min_heap) else -1 
    if least_upperhalf!=-1:
        heapq.heappush(min_heap,least_upperhalf)
    if x >= least_upperhalf :
        heapq.heappush(min_heap,x) # insert in min_heap
    else:
        heapq.heappush(max_heap,-1*x)
