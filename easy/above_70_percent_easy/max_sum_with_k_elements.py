"""
You are given a 0-indexed integer array nums and an integer k. Your task is to perform the following operation exactly
k times in order to maximize your score:

Select an element m from nums.
Remove the selected element m from the array.
Add a new element with a value of m + 1 to the array.
Increase your score by m.
Return the maximum score you can achieve after performing the operation exactly k times.
"""
from typing import List


def max_sum(nums: List[int], k: int) -> int:
    max_num = max(nums)
    result = max_num
    for i in range(k - 1):
        max_num += 1
        result += max_num
    return result

if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    k = 3
    print(max_sum(nums, k))
