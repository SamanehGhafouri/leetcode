"""
Given an integer array nums and an integer k,
return the number of pairs (i, j) where
i < j such that |nums[i] - nums[j]| == k.

The value of |x| is defined as:

x if x >= 0.
-x if x < 0.
"""
from typing import List


def count_k_difference(nums: List[int], k: int) -> int:
    count = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] < nums[j] and abs(nums[i] - nums[j]) == k:
                count += 1
    return count


if __name__ == '__main__':
    li = [3, 2, 1, 5, 4]
    k = 2
    print(count_k_difference(li, k))
