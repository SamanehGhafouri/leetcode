"""
You are given a positive integer array nums.

The element sum is the sum of all the elements in nums.
The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
Return the absolute difference between the element sum and digit sum of nums.

Note that the absolute difference between two integers x and y is defined as |x - y|.
"""
from typing import List


def diff_of_sum(nums: List[int]) -> int:
    sum_digits = 0
    for num in nums:
        sum_digit = 0
        for n in str(num):
            sum_digit += int(n)
        sum_digits += int(sum_digit)
    return abs(sum(nums) - sum_digits)


if __name__ == '__main__':
    nums = [1, 15, 6, 3]
    print(diff_of_sum(nums))
