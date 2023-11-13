"""
You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff.
A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets.
"""
from typing import List


def arithmetic_triplets(nums: List[int], diff: int) -> int:
    count_arithmetic_triplets = 0
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            for k in range(2, len(nums)):
                if nums[k] - nums[j] == diff and nums[j] - nums[i] == diff:
                    count_arithmetic_triplets += 1
    return count_arithmetic_triplets

if __name__ == '__main__':
    nums = [0, 1, 4, 6, 7, 10]
    diff = 3
    print(arithmetic_triplets(nums, diff))