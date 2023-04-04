from os import *
from sys import *
from collections import *
from math import *

def uniqueSubstrings(input) :
    # hash map to track which letter occured recently at which index
    # if we see any occurance we simply shift our left pointer to avoid repetation in the range left -> right
    hash_map = {}
    max_length_seen_so_far = 0
    left = 0
    for index, charAt in enumerate(input):
        # if we see current character is already visited in earlier index and we have to make sure our left pointer will never go back.
        if charAt in hash_map and hash_map[charAt] >= left:
            left = hash_map[charAt] + 1
        # update for every character traversal - so we can know when recently it has occured.
        hash_map[charAt] = index
        # keep track of max length
        max_length_seen_so_far = max(max_length_seen_so_far, len(input[left: index + 1]))
    return max_length_seen_so_far

print(uniqueSubstrings("abccdenghiqa"))