"""
Given an array nums of integers, return how many of them contain an even number of digits.
"""
from typing import List
import math


def find_numbers(nums: List[int]) -> int:
    count = 0
    for i in nums:
        digits_after_log = math.log10(i)
        floor_log_num = math.floor(digits_after_log)
        if floor_log_num > 0 and floor_log_num % 2 != 0:
            count += 1
    return count


if __name__ == '__main__':
    arr = [555, 901, 482, 1771]
    print(find_numbers(arr))
