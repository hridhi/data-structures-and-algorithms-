#finding the kth smallest element in the array given using heap
import heapq
#to convert a list into heap 
#heapq.heappush(H,8)
#heapq.heapreplace(H,6)
def kmin(a,k):
  n=len(a)
  heapq.heapify(a)
  for i in range(k-1):
    heapq.heappop(a)
  m=heapq.heappop(a)
  return m

a=[1,2,3,4,5]
k=2
m=kmin(a,k)
print("kth minimum")
print(m)
