"""
You are given a 1-indexed integer array nums of length n.

An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.

Return the sum of the squares of all special elements of nums.
"""
from typing import List


def sum_of_squares(nums: List[int]) -> int:
    sum_square = 0
    for i in range(len(nums)):
        if len(nums) % (i + 1) == 0:
            sum_square += nums[i] * nums[i]
    return sum_square


if __name__ == '__main__':
    nums = [2, 7, 1, 19, 18, 3]
    print(sum_of_squares(nums))
