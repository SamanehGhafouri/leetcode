"""
You are given an integer array nums consisting of 2 * n integers.

You need to divide nums into n pairs such that:

Each element belongs to exactly one pair.
The elements present in a pair are equal.
Return true if nums can be divided into n pairs, otherwise return false.
"""
import collections
from typing import List


def divide_array(nums: List[int]) -> bool:
    set_nums = set(nums)
    dict_nums = collections.Counter(nums)
    count_even_val = 0
    for k, v in dict_nums.items():
        if v % 2 == 0:
            count_even_val += 1
    if count_even_val == len(set_nums):
        return True
    return False


if __name__ == '__main__':
    li = [3, 2, 3, 2, 2, 2]
    print(divide_array(li))
