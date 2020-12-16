#Given two strings A and B, the task is to convert A to B if possible. The only operation allowed is to put any character from A and insert it at front.
#Find if it’s possible to convert the string. If yes, then output minimum no. of operations required for transformation
def string_to_string(A,B):
    count=0
    n=len(A)
    while n>=0:
        if B[n-1]==A[n-1]:
            n=n-1
        else:
            count+=1
            temp=A[n-1]
            for i in range(n-1):
                A[n-1-i]=A[n-2-i]
            A[0]=temp
    return count

A="EACBD"
B="EABCD"
x=string_to_string(A,B)
print(x)
