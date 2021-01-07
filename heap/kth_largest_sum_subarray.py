def Kth_largest_sum(arr,n,k):
  sum=[]
  sum.append(0)
  sum.append(arr[0])
  for i in range(2,n+1):
    sum.append(arr[i-1]+sum[i-1]) 
  q=[]
  heapq.heapify(q)
  for i in range(1,n+1):
    for j in range(i,n+1):
      x=sum[j]-sum[i-1]
      if len(q)<k:
        heapq.heappush(q,x)
      else:
        if q[0]<x:
          #to check sums between different subarrays 
          heapq.heappop(q)
          heapq.heappush(q,x)
  return q[0]
          
