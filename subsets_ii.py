from typing import List
from collections import Counter


def uniqueSubsets(n :int, arr :List[int]) -> List[List[int]]:
    subsets = []
    array = [0 for _ in range(101)]
    arr.sort()
    for key in arr:
        array[key]+=1
    
    # Traversal
    def traversal(subset, index):
        if index == len(arr):
            subsets.append(subset.copy())
            return
        
        # Left Part 
        value = arr[index]
        if array[value] > 0:
            array[value] -= 1
            traversal(subset + [value], index + 1)
            array[value] += 1

        # Right Part
        temp = array[value] 
        array[value] = 0
        traversal(subset, index + 1)
        array[value] = temp

    traversal([], 0)
    return subsets

# arr = [1, 2, 2, 3]
# print(uniqueSubsets(len(arr), arr))


arr = [5, 0, 7, 0]
print(uniqueSubsets(len(arr), arr))