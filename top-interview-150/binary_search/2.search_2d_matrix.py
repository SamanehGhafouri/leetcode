"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""
from typing import List


def binary_search(nums, target):
    low, high = 0, len(nums)
    while low < high:
        mid = (low + high) // 2
        if target == nums[mid]:
            return True
        elif target > nums[mid]:
            low = mid + 1
        elif target < nums[mid]:
            high = mid
    return False


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    for nums in matrix:
        if target > nums[-1]:
            continue
        return binary_search(nums, target)


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    print(search_matrix(matrix, target))
