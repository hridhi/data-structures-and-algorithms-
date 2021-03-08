'''
Given an array of integers (A[])  and a number x, find the smallest subarray with sum greater than the given value.

Note: The answer always exists. It is guaranteed that x doesn't exceed the summation of a[i] (from 1 to N).
'''
def smallestSubWithSum(arr, n, x):
 
    min_len = n + 1
 
   for start in range(0,n):
        curr_sum = arr[start]
 
            if (curr_sum > x):
            return 1
 
       
        for end in range(start+1,n):
         
           
            curr_sum += arr[end]
 
            
            if curr_sum > x and (end - start + 1) < min_len:
                min_len = (end - start + 1)
         
    return min_len;
 
 
# Driver program to test above function */
arr1 = [1, 4, 45, 6, 10, 19]
x = 51
n1 = len(arr1)
res1 = smallestSubWithSum(arr1, n1, x);
if res1 == n1+1:
    print("Not possible")
else:
    print(res1)
 
arr2 = [1, 10, 5, 2, 7]
n2 = len(arr2)
x = 9
res2 = smallestSubWithSum(arr2, n2, x);
if res2 == n2+1:
    print("Not possible")
else:
    print(res2)
 
arr3 = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
n3 = len(arr3)
x = 280
res3 = smallestSubWithSum(arr3, n3, x)
if res3 == n3+1:
    print("Not possible") 
else:
    print(res3)
