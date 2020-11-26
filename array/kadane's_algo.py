#finding continus subarray such that the sum is maximum 
def kadane(a):
  max_so_far=0
  max_end=0
  for i in range(len(a)):
    max_end=max_end+a[i]
    if max_end<0:
      max_end=0
    if max_so_far<max_end:
      max_so_far=max_end
  return max_so_far
a=[-1,4,-2,5,10]
print(kadane(a))
#answer should be 4+(-2)+5+10
