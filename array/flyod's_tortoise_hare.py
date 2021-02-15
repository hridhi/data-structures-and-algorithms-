'''finding the duplicates in an array which contains n+1 integers 
using floyd's tortoise and hare cycle detection '''

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

