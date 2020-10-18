#we need to find the next lexiographic permutation of the given permutation and if the given permutation is last one then it should return the first permutation 
# we can do this by listing out all the permutations and then checking linearly which permutation will come next 
# the other method is as follows 
def nextPerm(a):
  count=0
  for i in range(len(a)-2,-1,-1):
    if(a[i]<a[i+1]):
      count=1
      break
  if(count==0):
    a.sort()#it just sorts but doesnt return anything 
    return a
  x=i
  for i in range(len(a)-1,-1,-1):
    if(a[i]>a[x]):
      a[i],a[x]=a[x],a[i]
      break
  y=int((len(a)-x-1)/2)
  k=0
  for i in range(x+1,y+2):
    a[i],a[len(a)-1-k]=a[len(a)-1-k],a[i]
    k=k+1
  return a

a=[3,2,1]
print(nextPerm(a))
