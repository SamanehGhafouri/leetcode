"""
Given an array of integers arr, return true if the number of occurrences of
each value in the array is unique, or false otherwise.
"""
import collections
from typing import List


def unique_occurrences(arr: List[int]) -> bool:
    dict_arr = collections.Counter(arr)
    set_occurrences = {val for key, val in dict_arr.items()}
    return len(dict_arr) == len(set_occurrences)


if __name__ == '__main__':
    ar = [1, 2, 2, 1, 1, 3]
    print(unique_occurrences(ar))
