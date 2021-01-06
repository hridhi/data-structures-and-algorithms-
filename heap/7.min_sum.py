def solve(self, arr, n):
        # code hera=b=0
        a=b=0
        heapq._heapify_min(arr)
        for i in range(n):
            if i%2==0:
                a*=10
                a+=heapq.heappop(arr)
            else:
                b*=10
                b+=heapq.heappop(arr)
        res=a+b
        return res 
