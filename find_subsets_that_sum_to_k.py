def print_all_subsequences(arr):
    paths = []

    def traversal(idx, path):

        # print and exit
        if idx >= len(arr):
            paths.append(path.copy())
            return
        # take 
        path.append(arr[idx])
        traversal(idx + 1, path)

        # dont take
        path.pop()
        traversal(idx + 1, path)

    traversal(0, [])

    return paths

def print_all_subsequences_sum_to_k(arr, target):
    paths = []

    def traversal(idx, path, path_sum):

        if idx >= len(arr):
            # print only if sum matches
            if target == path_sum:
                paths.append(path.copy())
            return
        
        # take 
        path.append(arr[idx])
        path_sum += arr[idx]
        traversal(idx + 1, path, path_sum)

        # dont take
        path.pop()
        path_sum -= arr[idx]
        traversal(idx + 1, path, path_sum)

    traversal(0, [], 0)

    return paths

def count_all_subsequences_that_sum_to_k(arr, target):
    def traversal(idx, path, path_sum):
        if idx >= len(arr):
            # return 1 only if count matches target
            return 1 if (target == path_sum) else 0
        
        # take 
        path.append(arr[idx])
        path_sum += arr[idx]
        left = traversal(idx + 1, path, path_sum)

        #  dont take
        path.pop()
        path_sum -= arr[idx]
        right = traversal(idx + 1, path, path_sum)

        # sum of left and right as we are counting
        return left + right
    return traversal(0, [], 0)

def print_any_one_subsequence_that_sum_to_k(arr, target):

    def traversal(idx, path, path_sum):

        if idx >= len(arr):
            if target == path_sum:
                print(path.copy())
            # return true if match else false
            return target == path_sum
        
        # Take
        path.append(arr[idx])
        path_sum += arr[idx]
        left = traversal(idx + 1, path, path_sum)

        # Dont take
        path.pop()
        path_sum -= arr[idx]
        # search right only if left has no found
        right = traversal(idx + 1, path, path_sum) if not left else False

        # if any one of them has match then result will be a match

        return right or left
    return traversal(0, [], 0)
    

arr = [1,3,4,2,2]
print(print_all_subsequences(arr))
print(print_all_subsequences_sum_to_k(arr, 4))
print(count_all_subsequences_that_sum_to_k(arr, 4))
print_any_one_subsequence_that_sum_to_k(arr, 4)