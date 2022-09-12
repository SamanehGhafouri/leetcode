"""
You are given an array of integers nums. You are also given an integer original which is the
first number that needs to be searched for in nums.

You then do the following steps:

If original is found in nums, multiply it by two (i.e., set original = 2 * original).
Otherwise, stop the process.
Repeat this process with the new number as long as you keep finding the number.
Return the final value of original.
"""
from typing import List
from easy.above_70_percent_easy.Algorithms.binary_search import BinarySearch


def find_final_value(nums: List[int], original: int) -> int:
    binary_obj = BinarySearch()
    nums.sort()
    for _ in nums:
        if original > nums[-1]:
            return original
        else:
            if binary_obj.binary_search(nums, original, 0, len(nums)) is False:
                return original
            else:
                original = original * 2
    return original


if __name__ == '__main__':
    arr = [5, 3, 6, 1, 12]
    print(find_final_value(arr, 3))
