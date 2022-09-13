"""
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.
"""
from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1).intersection(set(nums2)))


if __name__ == '__main__':
    arr1 = [4, 9, 5]
    arr2 = [9, 4, 9, 8, 4]
    print(intersection(arr1, arr2))
