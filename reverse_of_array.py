
def reverse(a):
    start=0
    end=len(a)-1
    while(start<end):#this condition 
        a[start],a[end]=a[end],a[start] #reducing the number of lines 
        end=end-1
        start=start+1
    return a

a=[1,2,3,4,5]
reverse(a)
print("the reversed array is :")
print(a)
