"""
You are given a 0-indexed array of positive integers nums. Find the number of triplets (i, j, k) that meet the following conditions:

0 <= i < j < k < nums.length
nums[i], nums[j], and nums[k] are pairwise distinct.
In other words, nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k].
Return the number of triplets that meet the conditions.
"""
from typing import List


def unique_triplets(nums: List[int]) -> int:
    num_triplets = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                    num_triplets += 1
    return num_triplets
if __name__ == '__main__':
    nums = [4, 4, 2, 4, 3]
    print(unique_triplets(nums))
