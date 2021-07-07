#You are given a number of sticks of varying lengths. You will iteratively cut the sticks into smaller sticks, 
#discarding the shortest pieces until there are none left. At each iteration you will determine the length of the shortest 
#stick remaining, cut that length from each of the longer sticks and then discard all the pieces of that shortest length. 
#When all the remaining sticks are the same length, they cannot be shortened so discard them.

#Given the lengths of  sticks, print the number of sticks that are left before each iteration until there are none left.
def cutTheSticks(arr):
    # Write your code here
    arr.sort()
    res=[]
    while(arr):
        temp=1
        res.append(len(arr))
        for i in range(1,len(arr)):
            arr[i]=arr[i]-arr[0]
        #print(arr[i])
            if arr[i]==0:
                temp+=1
    
        arr=arr[temp:]
        #print(arr)
    return res 
    
