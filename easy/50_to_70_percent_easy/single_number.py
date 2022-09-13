"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""
import collections
from typing import List


def single_number(nums: List[int]) -> int:
    return {key for key, val in collections.Counter(nums).items() if val == 1}.pop()


if __name__ == '__main__':
    arr = [4, 1, 2, 1, 2]
    print(single_number(arr))
