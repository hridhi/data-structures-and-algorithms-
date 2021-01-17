t=int(input())
for i in range(t):
    m,n=map(int,input().split())
    arr1=list(map(int,input().split()))
    arr2=list(map(int,input().split()))
    #checking if arr2 is subset of arr1 or not 
    flag=0
    for i in arr2:
        if i not in arr1:
            flag=1
    if flag==1:
        print("No")
    else:
        print("Yes")
    # we can use some good operator and make it simple in time 
    #if l1&l2 == l2 : print ("Yes")
    # and is possible for set so convert the list to set 
