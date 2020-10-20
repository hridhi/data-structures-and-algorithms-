#Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.
# brute force 
# we can run 2 different loops and find out the pairs which will take O(n^2) time complexity 
#another approach 
# we an firstly create a map initialized to 0 and then if element is encountered in the array we increment 
# next step is we check m[sum-a[i]] if it is one then we add it to the count 
# next step is eliminating  a[i]+a[i] pair by decrementing the count by 1 every time we encounter 
# next is to divide the count by 2 as we will count each pair twice and hence we get the answer 
