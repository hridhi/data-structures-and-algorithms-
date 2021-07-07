#code
#pattern formation 
#pascals triangle 
rows=3
list1=[]
for i in range(rows):
    temp=[]
    for j in range(i+1):
        if j==0 or j==i:
            temp.append(1)
        else:
            temp.append(list1[i-1][j-1]+list1[i-1][j])
    list1.append(temp)
#print(list1)
for i in range(rows):
    for j in range(rows-i-1):
        print("",end=" ")
    for j in range(i+1):
        print(list1[i][j],end=" ")
    print()
            
