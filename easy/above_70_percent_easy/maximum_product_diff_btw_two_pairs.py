"""
The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
Given an integer array nums, choose four distinct indices w, x, y, and z such that the product
difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference.
"""
from typing import List


def max_product_diff(nums: List[int]) -> int:
    sorted_nums = sorted(nums)
    w, x, y, z = sorted_nums[0], sorted_nums[1], sorted_nums[-2], sorted_nums[-1]
    return (y * z) - (w * x)


if __name__ == '__main__':
    li_nums = [4, 2, 5, 9, 7, 4, 8]
    "expected_value = 64"
    print(max_product_diff(li_nums))
