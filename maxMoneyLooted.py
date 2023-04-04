from sys import stdin
from typing import List

def maxMoneyLooted(arr) :
    memory = {}
    def traverse(idx):

        if idx < 0:
            return 0
        
        if idx in memory:
            return memory[idx]
        
        pick = arr[idx] + traverse(idx - 2)

        not_pick = 0 + traverse(idx - 1)

        memory[idx] = max(pick, not_pick)

        return memory[idx]

    return traverse(len(arr) - 1)

# along the circle 
def rob(self, arr: List[int]) -> int:
    if len(arr) == 1:
        return arr[0]
    memory = {}
    def traverse(idx):

        if idx < 0:
            return 0
        
        if idx in memory:
            return memory[idx]
        
        pick = arr[idx] + traverse(idx - 2)

        not_pick = 0 + traverse(idx - 1)

        memory[idx] = max(pick, not_pick)

        return memory[idx]

    option_a = traverse(len(arr) - 2)
    memory = {}
    arr.pop(0)
    option_b = traverse(len(arr) - 1)
    return max(option_a, option_b)

print(maxMoneyLooted([2, 1, 4, 9]))
print(maxMoneyLooted([2]))
print(maxMoneyLooted([2, 5]))
print(maxMoneyLooted([2, 1, 4]))
print(maxMoneyLooted([]))

