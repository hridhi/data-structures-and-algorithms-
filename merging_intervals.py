#given a list of intervals we need to merge them to get fewer number of intervals 
# we can use a naive approach where we check a given interva with every other interval and this will take O(n^2) complexity 
# we can sort the values by their start position and check as well which will take less complexity than before 
def merge(a):
  a.sort(key=lambda x:x[0])#sorting the array with lambda function
  m=[]
  m.append(a[0])
  k=1
  for i in range(1,len(a)):
    if(a[i][0]<=m[k-1][1]):
      if(m[k-1][1]<a[i][1]):
        m[k-1][1]=a[i][1]
    else:
      m.append(a[i])
      k=k+1
  return m

a=[[6,8],[1,9],[2,4],[4,7],[11,12],[0,1]]
print(merge(a))
