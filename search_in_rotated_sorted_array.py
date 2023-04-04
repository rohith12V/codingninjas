def search(source, target) :
    def performBST(arr, low, high):
        if low > high:
            return -1
        mid = (low + high ) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return performBST(arr, low, mid - 1)
        else:
            return performBST(arr, mid + 1, high)
    # find pivot
    pivot = len(arr) - 1
    for index in range(1, len(arr)):
        # p p 
        if arr[index] > arr[index - 1]:
            pivot = index - 1
            break
        # p n 
        if arr[index - 1] >= 0 and arr[index] < 0:
            pivot = index - 1
            break

    l_ans = performBST(0, pivot + 1)
    r_ans = performBST(pivot, len(arr) - 1)
    return l_ans if l_ans != -1 else r_ans

arr = [10, 12, 13, -3, -1, 0, 4, 7, 8, 9]
to_find = [-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
for f in to_find:
    print(search(arr, f))


# -1
# -1
# 3
# -1
# 4
# 5
# -1
# -1
# -1
# 6
# -1
# -1
# 7
# 8
# 9
# 0
# -1
# 1
# 2