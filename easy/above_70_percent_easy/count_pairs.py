"""
Given a 0-indexed integer array nums of length n and an integer target, return the number of
pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.
"""
from typing import List


def count_pairs(nums: List[int], target: int) -> int:
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            num_i = nums[i]
            num_j = nums[j]
            sum_nums = num_i + num_j
            if sum_nums < target:
                count += 1
    return count


if __name__ == '__main__':
    nums = [-6, 2, 5, -2, -7, -1, 3]
    target = -2
    print(count_pairs(nums, target))
