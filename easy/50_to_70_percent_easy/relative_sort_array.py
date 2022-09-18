"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.
Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.
"""
import collections
from typing import List


def relative_sort_array(arr1: List[int], arr2: List[int]) -> List[int]:
    dict_ar1 = collections.Counter(arr1)
    new_arr = []
    for num in arr2:
        if num in dict_ar1:
            [new_arr.append(num) for _ in range(dict_ar1[num])]

    for num in new_arr:
        arr1.remove(num)
    arr1.sort()
    return new_arr + arr1


if __name__ == '__main__':
    ar1 = [2, 21, 43, 38, 0, 42, 33, 7, 24, 13, 12, 27, 12, 24, 5, 23, 29, 48, 30, 31]
    ar2 = [2, 42, 38, 0, 43, 21]
    print(relative_sort_array(ar1, ar2))
