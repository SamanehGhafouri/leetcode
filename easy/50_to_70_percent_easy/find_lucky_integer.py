"""
Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.
"""
import collections
from typing import List


def find_lucky(arr: List[int]) -> int:
    dict_arr = collections.Counter(arr)
    max_num = -1
    for k, v in dict_arr.items():
        if k == v:
            if k > max_num:
                max_num = k
    return max_num

if __name__ == '__main__':
    arr = [1,2,2,3,3,3]
    print(find_lucky(arr))