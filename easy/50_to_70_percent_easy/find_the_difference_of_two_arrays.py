"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.
"""
from typing import List


def find_difference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    result = []
    set_nums1 = set(nums1)
    set_nums2 = set(nums2)
    intersection = set_nums1.intersection(set_nums2)
    result.append(list(set_nums1 - intersection))
    result.append(list(set_nums2 - intersection))
    return result


if __name__ == '__main__':
    nums1 = [1, 2, 3, 3]
    nums2 = [1, 1, 2, 2]
    print(find_difference(nums1, nums2))
