"""
You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions
are satisfied:

Every element less than pivot appears before every element greater than pivot.
Every element equal to pivot appears in between the elements less than and greater than pivot.
The relative order of the elements less than pivot and the elements greater than pivot is maintained.
More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of
the jth element. For elements less than pivot, if i < j and nums[i] < pivot and nums[j] < pivot, then pi < pj.
Similarly for elements greater than pivot, if i < j and nums[i] > pivot and nums[j] > pivot, then pi < pj.
Return nums after the rearrangement.
"""
from typing import List


def pivot_array(nums: List[int], pivot: int) -> List[int]:
    pivot_li = []
    less_than_pivot = []
    greater_than_pivot = []
    for n in nums:
        if n == pivot:
            pivot_li.append(n)
        elif n > pivot:
            greater_than_pivot.append(n)
        else:
            less_than_pivot.append(n)
    return less_than_pivot + pivot_li + greater_than_pivot


if __name__ == '__main__':
    nums = [9, 12, 5, 10, 14, 3, 10]
    pivot = 10
    print(pivot_array(nums, pivot))
