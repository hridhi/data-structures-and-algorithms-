#we will be given an array of both positive , negative and zero numbers in the array 
#approach one is we can check linearly if the sum or the number is less than the previous sum then change the sum 
# if the sum becomes 0 at some point then return TRUE 
#approach 2 
#We can also use hashing. The idea is to iterate through the array and for every element arr[i], calculate sum of elements form 0 to i
#if the sums repeat then return TRUE as the array will have a sum comtaining 0 
