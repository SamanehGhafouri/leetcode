"""
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn)
such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
"""
from typing import List


def array_pair_sum(nums: List[int]) -> int:
    sorted_nums = sorted(nums)
    maxim_sum = 0

    for i in range(len(sorted_nums) // 2):
        maxim_sum += sorted_nums[0]
        sorted_nums.pop(0)
        sorted_nums.pop(0)
    return maxim_sum


if __name__ == '__main__':
    arr = [1, 4, 3, 2]
    print(array_pair_sum(arr))
