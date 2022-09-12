"""
Given a 0-indexed integer array nums of length n and an integer k,
return the number of pairs (i, j) where 0 <= i < j < n,
such that nums[i] == nums[j] and (i * j) is divisible by k.
"""
from typing import List


def count_pairs(nums: List[int], k: int) -> int:
    count = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if 0 <= i < j and nums[i] == nums[j] and (i * j) % k == 0:
                count += 1
    return count


if __name__ == '__main__':
    nums_li = [3, 1, 2, 2, 2, 1, 3]
    k_int = 2
    print(count_pairs(nums_li, k_int))
