"""
Given the array of integers nums, you will choose two different indices i and j of that array.
Return the maximum value of (nums[i]-1)*(nums[j]-1).
"""
from typing import List


def max_product(nums: List[int]) -> int:
    sorted_nums = sorted(nums)
    max_prod = (sorted_nums[-1] - 1) * (sorted_nums[-2] - 1)
    return max_prod


if __name__ == '__main__':
    arr = [1, 5, 4, 5]
    print(max_product(arr))
