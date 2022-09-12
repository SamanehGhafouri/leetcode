"""
You are given an integer array nums. The unique elements of an array are
the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.
"""
import collections
from typing import List


def sum_of_unique_elements(nums: List[int]) -> int:
    nums_dict = collections.Counter(nums)
    total_unique_some = 0
    for k in nums_dict:
        if nums_dict[k] == 1:
            total_unique_some += k
    return total_unique_some


if __name__ == '__main__':
    li = [1, 2, 3, 2]
    print(sum_of_unique_elements(li))
