"""
Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
"""

import math
from typing import List


def find_gcd(nums: List[int]) -> int:
    sorted_nums = sorted(nums)
    smallest_num = min(sorted_nums)
    largest_num = max(sorted_nums)
    return math.gcd(smallest_num, largest_num)


if __name__ == '__main__':
    arr = [2, 5, 6, 9, 10]
    print(find_gcd(arr))
