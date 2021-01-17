def solution(arr,n,k):
    req=n//k
    d=dict()
    for ele in arr:
        if ele in d.keys():
            d[ele]+=1
        else:
            d[ele]=1
    #d=dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))
    for x,y in d.items():
        if y>req:
            print(x,end=" ")


arr=[3,1,2,2,2,1,4,3,3]
n,k=9,4
solution(arr,n,k)
# can also be solved by using hashing approach 
