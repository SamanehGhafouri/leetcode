"""
Given an integer array nums that does not contain any zeros, find the largest positive integer k such that
-k also exists in the array.

Return the positive integer k. If there is no such integer, return -1.
"""
from typing import List


def find_max_k(nums: List[int]) -> int:
    set_positive = set()
    set_negative = set()
    for num in nums:
        if num > 0:
            set_positive.add(num)
        if num < 0:
            set_negative.add(num)
    if len(set_positive) == 0 or len(set_negative) == 0:
        return - 1
    sorted_positives = sorted(set_positive)
    for num in range(len(set_positive)):
        max_num = sorted_positives[-1]
        negative_num = -abs(max_num)
        if negative_num in set_negative:
            return max_num
        else:
            sorted_positives.pop()
        if len(sorted_positives) == 0:
            return -1
    return max_num


if __name__ == '__main__':
    nums = [-1, 2, -3, 3]
    print(find_max_k(nums))
