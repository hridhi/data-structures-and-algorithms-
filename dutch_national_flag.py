#given an array containing 0's,1's,2's we need to sort it in ascending order 
#we can count the number of 0's , 1's and 2's and also solve this kind of problem like below
#a = [0,0,0]
#b=[0,0,1,2,1,2,0,1,2,0]
#for i in k:
    #A[int(i)]+=1
#print('0 '*A[0] + '1 '*A[1] + '2 '*A[2])

#this problem is application of dutch national flag algorithm where we consider 2 pointers lo and hi 
#all the elements below lo pointer are 0's and above hi  pointer are 2's in between are 1's and hence sorted as required 

def dutch(a):
  lo=0
  pointer=0
  hi=len(a)-1
  while pointer<=hi:
    if a[pointer]==0:
      a[lo],a[pointer]=a[pointer],a[lo]
      lo=lo+1
      pointer=pointer+1 #already it will be comparing and coming so updating pointer as well 
    elif a[pointer]==2:
      a[hi],a[pointer]=a[pointer],a[hi]
      hi=hi-1
    else:
      pointer=pointer+1
  return a

a=[0,1,2,0,1,2,1,0,2,0]
print("the required array is:")
print(dutch(a))
