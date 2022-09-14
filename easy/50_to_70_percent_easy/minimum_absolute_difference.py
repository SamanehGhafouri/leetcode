"""
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
"""
from typing import List


def minimum_abs_difference(arr: List[int]) -> List[List[int]]:
    result = []
    dict_diff_nums = {}
    arr.sort()
    for i in range(len(arr) - 1):
        diff = abs(arr[i] - arr[i + 1])
        dict_diff_nums[arr[i], arr[i + 1]] = diff

    minimum_diff = min(dict_diff_nums.values())

    for key, val in dict_diff_nums.items():
        if val == minimum_diff:
            result.append(list(key))
    return result


if __name__ == '__main__':
    # ar = [1, 3, 6, 10, 15]
    # ar = [3,8,-10,23,19,-4,-14,27]
    ar = [-17, 46, 63, 81, -101, -91, 121, -2, 112, -15, -65, -96, 6, -139]
    print(minimum_abs_difference(ar))
