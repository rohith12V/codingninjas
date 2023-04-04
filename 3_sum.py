from collections import defaultdict


def findTriplets(arr, n, k):
    result = []
    arr.sort()

    for index in range(0, len(arr)):
        residual_sum = k - arr[index]
        
        # avoid duplicates
        if index > 0 and arr[index]== arr[index - 1]:
            continue

        # 2 [pointer approach]

        index_x = index + 1
        index_y = len(arr) - 1

        while (index_y > index_x):
            sum_at_pointers = arr[index_y] + arr[index_x] 

            if (sum_at_pointers == residual_sum):
                result.append([arr[index_y], arr[index_x], arr[index]])

                # avoid duplicates
                index_x += 1
                while index_x < index_y and arr[index_x] == arr[index_x - 1]:
                    index_x += 1

                
                # avoid duplicates
                index_y -= 1
                while index_y > index_x and arr[index_y] == arr[index_y + 1]:
                    index_y -= 1

            elif (sum_at_pointers > residual_sum):
                index_y -= 1

            else:
                index_x += 1
    return result

# print(findTriplets([1,2,3,1,2,3], 6, 6))
# print(findTriplets([10, 5, 5, 5, 2], 5, 12))
print(findTriplets([1,1,1,1,3], 5, 5))
                                                         