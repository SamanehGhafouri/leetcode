"""
Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and
the number of negative integers.

In other words, if the number of positive integers in nums is pos and the number of negative integers is neg, then
return the maximum of pos and neg.
Note that 0 is neither positive nor negative.
"""
from typing import List


def maximum_count(nums: List[int]) -> int:
    pos, neg = 0, 0
    for n in nums:
        if n < 0:
            neg += 1
        elif n > 0:
            pos += 1
    return max(pos, neg)

if __name__ == '__main__':
    nums = [-2, -1, -1, 1, 2, 3]
    print(maximum_count(nums))