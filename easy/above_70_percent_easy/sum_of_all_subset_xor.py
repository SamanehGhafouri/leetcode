"""
The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
Given an array nums, return the sum of all XOR totals for every subset of nums.

Note: Subsets with the same elements should be counted multiple times.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.
"""
import itertools
from functools import reduce
from typing import List


def subset_xor_sum(nums: List[int]) -> int:
    list_subsets = []
    for i in range(len(nums) + 1):
        for subset in itertools.combinations(nums, i):
            list_subsets.append(list(subset))
    sum_xor = 0
    for li in list_subsets:
        if len(li) == 0:
            continue
        if len(li) == 1:
            sum_xor += li[0]
        else:
            subset_xor = reduce(lambda x, y: x ^ y, li)
            sum_xor += subset_xor
    return sum_xor


if __name__ == '__main__':
    arr = [5, 1, 6]
    print(subset_xor_sum(arr))
