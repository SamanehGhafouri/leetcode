"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right,
and replace the last element with -1.

After doing so, return the array.
"""
from typing import List


def replace_elements(arr: List[int]) -> List[int]:

    new_arr = []
    for i in range(len(arr) - 1):
        new_arr.append(max(arr[i+1:]))
    new_arr.append(-1)
    return new_arr


if __name__ == '__main__':
    li = [17, 18, 5, 4, 6, 1]
    print(replace_elements(li))

