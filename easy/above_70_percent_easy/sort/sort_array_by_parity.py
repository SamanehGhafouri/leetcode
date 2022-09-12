"""
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.
"""
from typing import List


def sort_array_by_parity(nums: List[int]) -> List[int]:
    evens = [e for e in nums if e % 2 == 0]
    odds = [o for o in nums if o % 2 != 0]
    return evens + odds


def sort_faster_solution(nums: List[int]) -> List[int]:
    evens = list(filter(lambda x: x % 2 == 0, nums))
    odds = list(filter(lambda x: x % 2 != 0, nums))
    return evens + odds


if __name__ == '__main__':
    li = [3, 1, 2, 4]
    li_2 = [1, 0, 3]
    print(sort_array_by_parity(li_2))
    print(sort_faster_solution(li))
