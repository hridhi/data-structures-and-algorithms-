#in the given array of both positive and negative numbers we should bring all the negative numbers to one side 
#in our case lets take it to the left 
# you can sort also and negative numbers will come to one side 
# you can also use one pointer approach and check and swap 
# i am going to implement the 2 pointer approach that is checking from both the ends and swapping and incrementing accordingly 

def negshift(a):
  n=len(a)
  p1=0
  p2=n-1
  while(p1<=p2):
    if(a[p1]<0 and a[p2]>0):
      p1=p1+1
      p2=p2-1
    elif(a[p1]>0 and a[p2]>0):
      p2=p2-1
    elif(a[p1]<0 and a[p2]<0):
      p1=p1+1
    elif(a[p1]>0 and a[p2]<0):
      a[p1],a[p2]=a[p2],a[p1]
      p1=p1+1
      p2=p2-1
  return a

a=[1,-1,3,9,-4]
print("the shifted array is :")
print(negshift(a))
