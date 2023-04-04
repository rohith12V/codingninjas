from os import *
from sys import *
from collections import *
from math import *

def getTrappedWater(arr, n) :
    # Approach # 1
    max_left = [arr[0] for _ in range(n)]
    max_right = [arr[-1] for _ in range(n)]

    # Populate with cummulative Left Maximum
    # ip       = 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1
    # max_left = 0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3
    index = 1
    for value in arr[1:]:
        max_left[index] = max(max_left[index - 1], value)
        index+=1

    # Populate with cummulative right max
    # ip       = 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1
    # max_left = 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1
    index = 1
    for value in arr[::-1][1:]:
        max_right[len(arr) - index - 1] = max(max_right[len(arr) - index], value)
        index+=1

    # calculate min at each point
    # - 0, 1, 1, 2, 2, 2, 2, 3, 2, 2 ,2, 1
    min_at_point = [min(max_left[index], max_right[index]) for index in range(n)]

    # traverse and calculate volume at each point if -ve discard.
    total_units = 0
    for index, value in enumerate(arr):
        units = min_at_point[index] - value
        # add to total only if it is positive.
        if units > 0:
            total_units+=units

    return total_units

# Two Pointers
def getTrappedWater_version2(arr, n) :
    # Approach # 1
    left = 0
    right = len(arr) - 1
    max_left = arr[left]
    max_right = arr[right]

    total_units = 0

    index = 0
    while left < right:
        units = min(max_left, max_right) - arr[index]
        if units > 0:
            total_units += units

        # if Left has low value then try to increase it and vice versa.
        if max_left < max_right:
            left+=1
        elif max_left > max_right:
            right-=1
        else:
            left+=1 # or right-=1
        
        max_left = max(max_left, arr[left])
        max_right = max(max_right, arr[right])
        index+=1

    return total_units

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# arr = [3 ,0 ,0, 2 ,0, 4]
print(getTrappedWater(arr, len(arr)))
print(getTrappedWater_version2(arr, len(arr)))