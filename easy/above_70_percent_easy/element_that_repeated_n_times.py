"""
You are given an integer array nums with the following properties:

nums.length == 2 * n.
nums contains n + 1 unique elements.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times.
"""
import collections
from typing import List


def repeated_n_times(nums: List[int]) -> int:
    repeated_nums = collections.Counter(nums)

    for k in repeated_nums:
        if repeated_nums[k] > 1:
            return k


if __name__ == '__main__':
    li = [5, 1, 5, 2, 5, 3, 5, 4]
    print(repeated_n_times(li))
