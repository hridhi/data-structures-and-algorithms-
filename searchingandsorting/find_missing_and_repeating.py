#User function Template for python3
#cyclic sort 

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        i = 0
        while i < len(arr):
            j = arr[i]-1
            if arr[i] != arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                i += 1

        res = []
        for idx, num in enumerate(arr):
            if num != idx + 1:
                res.append(num)
                res.append(idx + 1)

        return res
