#full pyramid of alphabets
rows=3
A=ord("A")
arr=[]
arr.append([chr(A)])
cnt=1
for k in range(rows):
    print("",end=" ")
print(chr(A),end="")
print()
for i in range(1,rows):
    temp=[]
    temp2=[]
    j=0
    req=((2*i)+1)//2+1
    for k in range(rows-i):
        print(" ",end="")
    while(j<req):
        #2*i+1 = total
        print(chr(A+cnt+j),end=" ")
        temp2.append(chr(A+cnt+j))
        j=j+1
    temp2=temp2[::-1]
    temp2=temp2[1:]
    for j in range(len(temp2)):
        print(temp2[j],end=" ")
    #temp=temp+temp2
    #arr.append(temp)
    print()
#print(arr)
    
    
    
