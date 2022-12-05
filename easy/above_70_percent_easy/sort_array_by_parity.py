"""
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.
"""
from typing import List


def sort_array_by_parity_II(nums: List[int]) -> List[int]:
    evens = []
    odds = []
    sorted_nums = []
    for i in nums:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)

    for i in range(len(nums)):
        if i % 2 == 0:
            sorted_nums.append(evens.pop(0))
        else:
            sorted_nums.append(odds.pop(0))
    return sorted_nums


if __name__ == '__main__':
    a = [3, 1, 4, 2]
    print(sort_array_by_parity_II(a))
