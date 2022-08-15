"""
You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order.
If there are no target indices, return an empty list. The returned list must be sorted in increasing order.
"""
from typing import List


def target_indices(nums: List[int], target: int) -> List[int]:
    sorted_nums = sorted(nums)
    result = []

    for i in range(len(sorted_nums)):
        if sorted_nums[i] == target:
            result.append(i)
    return result


if __name__ == '__main__':
    arr_nums = [1, 2, 5, 2, 3]
    target_num = 5
    print(target_indices(arr_nums, target_num))
