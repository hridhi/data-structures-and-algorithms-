#a very basic problem we are going to rotate it by one unit 
def rotate(a):
  x=a[len(a)-1]
  for i in range(len(a)-1,0,-1):
    a[i]=a[i-1]
  a[0]=x
  return a
a=[1,2,3,4,5]
print(rotate(a))
