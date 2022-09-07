"""
Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are
present in at least two out of the three arrays. You may return the values in any order.
"""
from typing import List


def two_out_of_three(num1: List[int], num2: List[int], num3: List[int]) -> List[int]:
    set_num1 = set(num1)
    set_num2 = set(num2)
    set_num3 = set(num3)

    intersect1 = set_num1.intersection(set_num2)
    intersect2 = set_num1.intersection(set_num3)
    intersect3 = set_num2.intersection(set_num3)
    union_all = intersect1.union(intersect2, intersect3)

    return list(union_all)


if __name__ == '__main__':
    li_1 = [1, 1, 3, 2]
    li_2 = [2, 3]
    li_3 = [3]
    print(two_out_of_three(li_1, li_2, li_3))
