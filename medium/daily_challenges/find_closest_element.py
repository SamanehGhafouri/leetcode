"""
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result
should also be sorted in ascending order.

    An integer a is closer to x than an integer b if:

    |a - x| < |b - x|, or
    |a - x| == |b - x| and a < b
"""
from typing import List
from bisect import bisect_left


def find_closest_elements(arr: List[int], k: int, x: int) -> List[int]:
    i = bisect_left(arr, x)
    li = []

    right_i = i
    left_i = i - 1
    while len(li) < k:
        if left_i < 0:
            li.append(arr[right_i])
            right_i += 1
        elif right_i >= len(arr):
            li.append(arr[left_i])
            left_i -= 1
        else:
            right_v = abs(arr[right_i] - x)
            left_v = abs(arr[left_i] - x)
            if right_v < left_v:
                li.append(arr[right_i])
                right_i += 1
            else:
                li.append(arr[left_i])
                left_i -= 1
    li.sort()
    return li


if __name__ == '__main__':
    ar = [2, 27]
    k = 2
    x = 26
    print(find_closest_elements(ar, k, x))
