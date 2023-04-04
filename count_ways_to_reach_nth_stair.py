from os import *
from sys import *
from collections import *
from math import *

def countDistinctWays(nStairs: int) -> int:
    dp = [-1 for _ in range(nStairs + 1)]
    def traversal(current_stair):
        if current_stair == nStairs:
            return 1
        if current_stair > nStairs:
            return 0
        if dp[current_stair] != -1:
            return dp[current_stair]
        dp[current_stair]  = (traversal(current_stair + 1) + traversal(current_stair + 2)) % (10**9 + 7)
        return dp[current_stair]
    dp[0] = traversal(0)
    return dp[0]

print(countDistinctWays(0))