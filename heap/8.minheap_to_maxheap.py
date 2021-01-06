def min_to_max_heap(arr,n):
  #bottom up approach
  i=n//2
  i=n//2
  while i>=0:
    arr=heapify(arr,n,i)
    i=i-1
  return arr
