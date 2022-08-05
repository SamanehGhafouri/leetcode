"""
Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

A subarray is a contiguous subsequence of the array.
"""
from typing import List


def sum_odd_length_sub_arrays(arr: List[int]) -> int:
    all_sum = 0
    arr_length = len(arr)
    for i in range(arr_length):
        for j in range(i, arr_length, 2):
            for k in range(i, j + 1, 1):
                all_sum += arr[k]
    return all_sum


if __name__ == '__main__':
    arr_1 = [1, 4, 2, 5, 3]
    print(sum_odd_length_sub_arrays(arr_1))
