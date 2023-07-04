"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
"""
import collections
from typing import List


def majority_element(nums: List[int]) -> int:
    dict_nums = collections.Counter(nums)
    majority_value = max(dict_nums.values())
    for k, v in dict_nums.items():
        if v == majority_value:
            return k


if __name__ == '__main__':
    n = [2, 2, 1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 6, 6, 6]
    print(majority_element(n))
