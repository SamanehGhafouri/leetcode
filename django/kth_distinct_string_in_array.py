"""
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr.
If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.
"""
import collections
from typing import List


def kth_distinct(arr: List[str], k: int) -> str:
    set_arr = set(arr)
    if len(set_arr) < k:
        return ""
    if len(arr) != 1 and len(set_arr) == 1:
        return ""

    if len(set_arr) == len(arr):
        return arr[k - 1]

    dict_arr = collections.Counter(arr)
    distinct_num_dict = {}
    for key, val in dict_arr.items():
        if val == 1:
            distinct_num_dict[key] = 0
    count = 0
    for i in range(len(arr)):
        if arr[i] in distinct_num_dict:
            count += 1
            distinct_num_dict[arr[i]] = count
    for key, val in distinct_num_dict.items():
        if val == k:
            return key
        if k not in distinct_num_dict.values():
            return ""


if __name__ == '__main__':
    li = ["d", "b", "c", "b", "c", "a"]
    k = 2
    print(kth_distinct(li, k))
