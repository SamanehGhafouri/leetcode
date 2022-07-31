"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.
"""

from typing import List


def num_identical_pairs(nums: List[int]) -> int:
    num_pairs = 0
    new_dict = {}
    for i in nums:
        if i not in new_dict:
            new_dict[i] = 1
        else:
            new_dict[i] += 1

    for k, v in new_dict.items():
        if v >= 2:
            num_pairs += v * (v - 1) // 2
    return num_pairs


if __name__ == '__main__':
    li = [1, 2, 3, 1, 1, 3]
    print(num_identical_pairs(li))
