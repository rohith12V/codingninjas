def minSumArr(arr):
    # Use absolute values to calculate difference which is close to zero
    arr = sorted(arr, key = lambda a : abs(a))
    min_cost = float("inf")
    indexX = 0
    indexY = indexX + 1

    while indexY < len(arr):
        min_cost  = min(min_cost, abs(arr[indexY] + arr[indexX]))
        indexY += 1
        indexX += 1
    return min_cost

print(minSumArr([1, 60, -10, 70, -80, 85]))