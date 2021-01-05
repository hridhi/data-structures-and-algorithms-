def sliding_window_max(arr,n,k):
	i = 0
	j = k-1
	heap = arr[i:j + 1]
	heapq._heapify_max(heap)
	print(heap[0], end =" ")
	left= arr[i]
	i+= 1
	j+= 1
	nexts = arr[j]
	while j < n:
		heap[heap.index(left)] = nexts
		heapq._heapify_max(heap)
		print(heap[0], end =" ")
		left = arr[i]
		i+= 1
		j+= 1
		if j < n:
			nexts = arr[j]
