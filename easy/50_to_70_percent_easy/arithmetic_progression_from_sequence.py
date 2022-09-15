"""
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive
elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression.
Otherwise, return false.
"""
from typing import List


def can_make_arithmetic_progression(arr: List[int]) -> bool:
    arr.sort()
    set_diffs = set()
    for i in range(len(arr) - 1):
        diff = arr[i + 1] - arr[i]
        set_diffs.add(diff)
    if len(set_diffs) == 1:
        return True
    return False


if __name__ == '__main__':
    ar = [1, 2, 3, 2, 5]
    print(can_make_arithmetic_progression(ar))
