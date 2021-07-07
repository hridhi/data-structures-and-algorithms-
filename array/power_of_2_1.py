#power of 2 or not 
'''method 1 
-> taking log base 2
'''
import math 
n=3
arr=[2,3,4]
cnt=0
for i in range(n):
    x=math.log10(arr[i])/math.log10(2)
    if math.ceil(x)==math.floor(x):
        print(arr[i],end=" ")
