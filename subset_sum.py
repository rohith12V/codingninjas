from typing import List


def subsetSum(num: List[int]) -> List[int]:
    result = []
    # num.append(0)
    def traversal(index, current_sum):
        # Base Case
        if index > len(num):
            return
            
        result.append(current_sum)

        for x_index in range(index + 1, len(num)):

            # make sure current_sum has the latest value as per the index which it currently is in
            traversal(x_index, current_sum + num[x_index])  
            
    traversal(0, num[0])
    return sorted(result)

print(subsetSum([0, 1, 2]))