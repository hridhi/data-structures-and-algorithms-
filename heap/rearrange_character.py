import heapq
    
    
for _ in range(int(input())):
    s = input()
    dct = dict()
    res = 1
    for i in s:
        dct[i] = dct.get(i,0)+1
        if(dct[i] > (len(s)+1)/2):
            res = 0
            break
    print(res)
