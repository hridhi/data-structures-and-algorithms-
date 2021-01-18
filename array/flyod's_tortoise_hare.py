# finding the duplicates in an array which contains n+1 integers 
# the naive approach will be checking each and every integer and this will take over O(n^2) complexity 
# we can sort the array and find the duplicate 
#else you can make the numbers in the array as keys of the dictionary and then whose ever keys value is 2 that is the duplicate 
#to get linear time complexity the elements should be stored in data structure so we can store it in a set , so if an element already in set then return it 

#else we can use floyd's tortoise and hare cycle detection algorithm for the following problem 
#this helps to detect the cycle by using 2 pointers tortoise and hare and where hare moves faster than tortoise
def floyd_tor_hare(a):
  tor=hare=a[0]
  #finding the intersection point which will be inside the loop  
  while True:
    tor=a[tor]
    hare=a[a[hare]]
    if tor==hare:
      break
  tor=a[0]
  #finding the entrance of the loop 
  while tor!=hare: 
    tor=a[tor]
    hare=a[hare]
  return tor

a=[2,5,9,6,9,3,8,9,7,1]
print(floyd_tor_hare(a))
