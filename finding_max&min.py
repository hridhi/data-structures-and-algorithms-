#given an array finding the max and min with comparing pairs 
def minmax(a):
  n=len(a)
  if(n%2==0):
    mn=min(a[0],a[1]) #inbuilt function usage
    mx=max(a[0],a[1])
    i=2
  else:
    mn=mx=a[0]
    i=1
  while(i<n):
    if(a[i]>a[i+1]):
      mx=max(a[i],mx)
      mn=min(a[i+1],mn)
    else:
      mx=max(a[i+1],mx)
      mn=min(a[i],mn)
    i+=2
  return mx,mn

a=[1,2,3,4,5]
mx,mn=minmax(a)
print("maximum")
print(mx)
print("minimum")
print(mn)
