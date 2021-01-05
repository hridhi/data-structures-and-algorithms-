def kLargest(self,arr, n, k):
	    z = []
        heapq._heapify_max(arr)
        for i in range(k):
            m = heapq._heappop_max(arr)
            z.append(m)
        return z
