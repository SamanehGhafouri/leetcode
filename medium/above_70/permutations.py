"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""
from typing import List


def permute(nums: List[int]) -> List[List]:
    result = []
    if len(nums) == 1:
        return [nums[:]]
    i = len(nums)
    while i >= 1:
        n = nums.pop(0)
        perms = permute(nums)

        for perm in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)
        i -= 1
    return result



if __name__ == '__main__':
    ls = [1, 2, 3]
    print(permute(ls))