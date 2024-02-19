"""
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should return the array of nums such that the the array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
"""
from typing import List


def rearrange_array(nums: List[int]) -> List[int]:
    result = []
    positive = []
    negative = []
    for n in nums:
        if n >= 0:
            positive.append(n)
        else:
            negative.append(n)
    for p, n in zip(positive, negative):
        result.append(p)
        result.append(n)
    return result


if __name__ == '__main__':
    nums = [3, 1, -2, -5, 2, -4]
    print(rearrange_array(nums))
