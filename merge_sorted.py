#given 2 arrays of different sizes we need to merge them without using any extra space , so we need to modify the given array 
#one solution can be add all the elements to the first array and then sort it 
#second can be by using 2 different pointers in 2 arrays and swapping which will take O(n^2) complexity 
#let us also see another method where we have 2 pointers one is at last but one position in frst array and other is in the last position of second array 
def merge(ar1, ar2, m, n): 
    for i in range(n-1, -1, -1):   
        last = ar1[m-1] 
        j=m-2
        while(j >= 0 and ar1[j] > ar2[i]): 
            ar1[j+1] = ar1[j] 
            j-=1 
        if (j != m-2 or last > ar2[i]): 
            ar1[j+1] = ar2[i] 
            ar2[i] = last
    return ar1,ar2
ar1 = [1, 5, 9, 10, 15, 20] 
ar2 = [2, 3, 8, 13] 
m = len(ar1) 
n = len(ar2)
ar1,ar2=merge(ar1,ar2,m,n)
print(ar1)
print(ar2)
