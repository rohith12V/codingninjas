# Input:  [1, 23, 12, 9, 30, 2, 50], K = 3
# Output: 50, 30, 23

# Input:  [11, 5, 12, 9, 44, 17, 2], K = 2
# Output: 44, 17

import heapq

def kLargest(arr, k):
    heap_list= []
    heapq.heapify(heap_list)
    for value in arr:
        heapq.heappush(heap_list, value)
        if len(heap_list) > k:
            heapq.heappop(heap_list)
    return heap_list

def kSmallest(arr, k):
    heap_list= []
    heapq.heapify(heap_list)
    for value in arr:
        heapq.heappush(heap_list, -value)
        if len(heap_list) > k:
            heapq.heappop(heap_list)
    return list(map(lambda x: x * -1, heap_list))

arr = [1, 23, 12, 9, 30, 2, 50]
k = 3
print(kLargest(arr, k))
print(kSmallest(arr, k))

