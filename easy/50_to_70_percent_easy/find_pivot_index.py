"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of
the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there
are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""
from typing import List


def pivot_index(nums: List[int]) -> int:
    pivot_i = -1
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i + 1:]):
            pivot_i = i
            break
    return pivot_i


if __name__ == '__main__':
    li = [-1, -1, 0, 0, -1, -1]
    print(pivot_index(li))
