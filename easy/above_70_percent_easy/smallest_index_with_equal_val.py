"""
Given a 0-indexed integer array nums, return the smallest index i of nums such that i mod 10 == nums[i],
or -1 if such index does not exist.

x mod y denotes the remainder when x is divided by y.
"""
from typing import List


def smallest_equal(nums: List[int]) -> int:
    result = []
    for i in range(len(nums)):

        if i % 10 == nums[i]:
            result.append(i)
    if len(result) == 0:
        return -1
    return min(result)


if __name__ == '__main__':
    arr = [4, 3, 2, 1]
    print(smallest_equal(arr))
