# A program to get the longest palindromic substring 

for _ in range(int(input())):
    n=input()
    sub=[]
    for l in range(len(n)+1):
        for i in range(len(n)-l+1):
            j=i+l-1
            x=""
            for k in range(i,j+1):
                x+=n[k]
            sub.append(x)
    req=""
    reqn=0
    for i in range(len(sub)):
        m=sub[i]
        k=m[::-1]
        if(m==k):
            if(len(m)>reqn):
                reqn=len(m)
                req=m
    print(req)
