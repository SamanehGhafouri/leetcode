"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return
the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


def search_insert(nums: List[int], target: int) -> int:

    low, high = 0, len(nums)
    while low < high:
        mid = (low + high) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            low = mid + 1
        elif target < nums[mid]:
            high = mid
    return low


if __name__ == '__main__':
    nums = [1, 3, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 17, 22, 44, 33, 88]
    target = 2
    print(search_insert(nums, target))
