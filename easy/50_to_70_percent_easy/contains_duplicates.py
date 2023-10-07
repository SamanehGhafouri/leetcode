"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""
from typing import List


def contains_duplicates(nums: List[int]) -> bool:
    if len(set(nums)) < len(nums):
        return True
    return False


if __name__ == '__main__':
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(contains_duplicates(nums))
