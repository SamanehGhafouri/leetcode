"""
You are given a 0-indexed integer array nums and an integer k.

Return an integer that denotes the sum of elements in nums whose corresponding indices have exactly k set bits
in their binary representation.

The set bits in an integer are the 1's present when it is written in binary.

For example, the binary representation of 21 is 10101, which has 3 set bits.
"""
from typing import List


def sum_indices_with_k_set_bits(nums: List[int], k: int) -> int:
    sum_i = 0
    for i in range(len(nums)):
        if str(bin(i)).count("1") == k:
            sum_i += nums[i]
    return sum_i


if __name__ == '__main__':
    nums = [5, 10, 1, 5, 2]
    k = 1
    print(sum_indices_with_k_set_bits(nums, k))
