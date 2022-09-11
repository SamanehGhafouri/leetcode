"""
Given an integer array nums sorted in non-decreasing order, return an array of the
squares of each number sorted in non-decreasing order.
"""
from typing import List


def sorted_squares(nums: List[int]) -> List[int]:
    squares = [i * i for i in nums]
    squares.sort()
    return squares


if __name__ == '__main__':
    li = [-4, -1, 0, 3, 10]
    print(sorted_squares(li))
