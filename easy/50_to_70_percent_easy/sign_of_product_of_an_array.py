"""
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).
"""
from typing import List


def array_sign(nums: List[int]) -> int:
    count_negatives = 0
    if 0 in set(nums):
        return 0
    for num in nums:
        if num < 0:
            count_negatives += 1
    if count_negatives % 2 == 0:
        return 1
    return -1


if __name__ == '__main__':
    arr = [-1, 1, -1, 1, -1]
    print(array_sign(arr))
