import heapq
def merge(numbers):
    # code here
    # return merged list
    a = []
    for i in numbers:
        a+=i
    res=[]
    heapq.heapify(a)
    while(len(a)):
        res.append(heapq.heappop(a))
    return res

numbers=[1 2 3],[4 5 6 ],[ 7 8 9 ]
