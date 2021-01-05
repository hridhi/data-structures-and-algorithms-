def heapify(arr,n,i):
  l=(2*i)+1
  r=(2*i)+2
  if l<n and arr[i]>arr[l]:
      arr[i],arr[l]=arr[l],arr[i]
      heapify(arr,n,l)
  if r<n and arr[i]>arr[r]:
      arr[i],arr[r]=arr[r],arr[i]
      heapify(arr,n,r)
  return arr   
    
def array_heap(arr,n):
  # for a min heap 
  #not considering the leaf nodes
  i=n//2
  while i>=0:
    arr=heapify(arr,n,i)
    i=i-1
  return arr

arr=[12,20,2,13,32,50,88,21,18,91]
n=10
x=array_heap(arr,n)
print(x)
