from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        combinations = []

        n = n + 1

        def traversal(index, path):
            if len(path) == k:
                combinations.append(path.copy())
                return
            for x_index in range(index, n):
                traversal(x_index + 1, path + [x_index])
        traversal(1, [])
        return combinations

print(Solution().combine(3, 2))