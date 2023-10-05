"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
"""
from typing import List


def permutation_unique(nums: List[int]) -> List[List[int]]:
    result = []
    if len(nums) == 1:
        return [nums[:]]
    i = len(nums)
    while i >= 1:
        n = nums.pop(0)
        perms = permutation_unique(nums)
        for perm in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)
        i -= 1
    result.sort()
    final = [result[0]]
    for l in result[1::]:
        if final[-1] != l:
            final.append(l)
    return final


if __name__ == '__main__':
    ls = [1, 1, 2]
    print(permutation_unique(ls))
