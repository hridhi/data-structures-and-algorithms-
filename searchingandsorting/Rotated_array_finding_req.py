piv=0
req=0
a=list(map(int,input().split()))
x=int(input())
for i in range(len(a)-1):
    if a[i]>a[i+1]:
        piv=i+1
if x>a[len(a)-1]:
    #before pivot elements binary search 
    l=0
    h=piv-1
    while True:
        mid=(l+h)//2
        if(a[mid]>x):
            h=mid-1
        if(a[mid]<x):
            l=mid+1
        else:
            req=mid
            break  
else:
    #after pivot elements binary search 
    l=piv
    h=len(a)-1
    while True:
        mid=(l+h)//2
        if(a[mid]>x):
            l=mid+1
        if(a[mid]<x):
            h=mid-1
        else:
            req=mid
            break
print(req)
