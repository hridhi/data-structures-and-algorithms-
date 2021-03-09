'''
Given an array arr of size N and an integer X. Find if there's a triplet in the array which sums up to the given integer X.
'''
class Solution:
    #User function Template for python3
    # arr[] : The input Array
    # N : Size of the Array
    # X : Sum which you need to search for 
    #Function to find if there exists a triplet in the 
    #array arr[] which sums up to X.
    def find3Numbers(self,arr, N, X):
        # Your Code Here
        arr.sort()
        for i in range(N-2):
            fix=arr[i]
            p1=i+1
            p2=N-1
            while(p1<p2):
                if arr[p1]+arr[p2]+fix>X:
                    p2=p2-1
                elif arr[p1]+arr[p2]+fix<X:
                    p1=p1+1
                else:
                    return 1
        return 0
