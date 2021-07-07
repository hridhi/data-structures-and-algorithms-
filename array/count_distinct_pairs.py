#Given an array arr[] of size N and an integer K, the task is to find the count of distinct pairs in the array whose sum is equal to K.


#arr=[5,6,5,7,7,8]
#k=13

arr=[2,6,7,1,8,3]
k=10
dic={}
cnt=0
for i in arr:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
#print(dic)
for i in arr:
    if 2*i==k:
        if dic[i]>1:
            cnt+=2
    if (k-i) in dic:
        del(dic[k-i])
        #print(i,k-i)
        #print(dic)
        cnt+=1
print(cnt//2)
