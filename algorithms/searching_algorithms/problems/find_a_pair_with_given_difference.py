# Input: arr[] = {5, 20, 3, 2, 50, 80}, n = 78
# Output: Pair Found: (2, 80)

# Input: arr[] = {90, 70, 20, 80, 50}, n = 45
# Output: No Such Pair

def find_pair_with_given_difference(arr, target):
    ds = {}
    for index, num in enumerate(arr):
        if (target + num) in ds:
            return (ds[target+num], index)
        if (num - target) in ds:
            return (ds[num - target], index)
        ds[num] =  index
    return (-1, -1)

print(find_pair_with_given_difference(
    [5, 20, 3, 2, 50, 80],
    15
))