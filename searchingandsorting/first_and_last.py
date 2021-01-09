def first(arr,x,n):
    l=0
    h=n-1
    res=-1
    while (l<=h):
        mid=(l+h)//2
        if arr[mid]>x:
            h=mid-1
        elif arr[mid]<x:
            l=mid+1
        else:
            res=mid
            h=mid-1
    return res 
def last(arr,x,n):
    l=0
    h=n-1
    res=-1
    while (l<=h):
        mid=(l+h)//2
        if arr[mid]>x:
            h=mid-1
        elif arr[mid]<x:
            l=mid+1
        else:
            res=mid
            l=mid+1
    return res
