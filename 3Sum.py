from collections import defaultdict

# You are given an array/list ARR consisting of N integers. Your task is to find all
# the distinct triplets present in the array which adds up to a given number K.
# example - 10 5 5 5 2, key = 12
# triplets = [[5 5 2]]


def findTriplets(arr, n, k):
    result = []

    # makes it easy to skip duplicates
    arr.sort()

    for index in range(0, len(arr)):
        # residual sum
        # eg: arr[index] = 10, key = 12 ; residual = 2 (we need to find 2 in the reminaing array i+1 -> n)
        residual_sum = k - arr[index]

        # avoid duplicates
        if index > 0 and arr[index] == arr[index - 1]:
            continue

        # 2 [pointer approach]

        index_x = index + 1
        index_y = len(arr) - 1

        while (index_y > index_x):

            sum_at_pointers = arr[index_y] + arr[index_x]

            if (sum_at_pointers == residual_sum):

                result.append([arr[index_y], arr[index_x], arr[index]])

                # avoid duplicates
                # residual = 7
                # index_x + index_y == 7 => pair = [5, 2, 5]
                # [5 (index), 2 (index_x), 2 [to_be_skipped], 4, 5 (index_y)]
                index_x += 1
                while index_x < index_y and arr[index_x] == arr[index_x - 1]:
                    index_x += 1

                # avoid duplicates
                index_y -= 1
                while index_y > index_x and arr[index_y] == arr[index_y + 1]:
                    index_y -= 1

            elif (sum_at_pointers > residual_sum):
                # reduce high so that our sum at pointers will also reduce
                index_y -= 1

            else:
                # increase low so that our sum at pointers will reach residual sum
                index_x += 1

    return result


print(findTriplets([1, 2, 3, 1, 2, 3], 6, 6))
print(findTriplets([10, 5, 5, 5, 2], 5, 12))
print(findTriplets([1, 1, 1, 1, 3], 5, 5))
