#Union of the two arrays can be defined as the set containing distinct elements from both the arrays. 
#If there are repetitions, then only one occurrence of element should be printed in union.

#the naive approach will be of making an array and copying all the elements of first array and checking and updating the union array with second array elements 
#else sorting and taking union is also possible 
#else in python make the array as set as set doesnt allow any duplicate values in it 
#Hashing is also a method of sorting key values in a database table in an efficient manner. so it could also be used here 

def union(a,b):
  u=set()
  for i in range(len(a)):
    u.add(a[i])
  for i in range(len(b)):
    u.add(b[i])
  return u
a=[1,2,3,4,5]
b=[4,5,6,7,3,5]
print(union(a,b))
