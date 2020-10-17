#we will be provided with a value k. We need to either increase or decrease element in the array by k (only once) where k > 0. such that the range will be minimum
def getMinDiff(a,k):
  if(len(a)==1): #case 1
    return 0
  else:
    a.sort() #sorting the array 
    m=a[0]+k
    mx=a[len(a)-1]-k
    if m>mx:                #case 5
      m,mx=mx,m
    for i in range(1,len(a)-1):
      sub=a[i]-k
      add=a[i]+k
      if (sub>m and add<mx): #case 2
        continue
      if(mx-sub <=add-m): #case 3
        m=sub
      else:       #case 4
        mx=add
  return mx-m

a=[1,15,10]
print(getMinDiff(a,6))
  
