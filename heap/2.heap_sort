def heapsort(arr,n):
  arr=array_heap(arr,n)
  #constructs a min heap 
  res=[]
  while n :
    res.append(arr[0])
    arr[0]=arr[n-1]
    n=n-1
    heapify(arr,n,0)
  return res 
