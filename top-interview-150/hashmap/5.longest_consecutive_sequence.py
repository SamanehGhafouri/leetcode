"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""
from typing import List


def longest_consecutive(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    set_nums = list(set(nums))
    set_nums.sort()
    if len(set_nums) == 1:
        return 1
    count_consecutive = set()
    tracker = set_nums[0]
    count = 0
    for n in set_nums[1::]:
        num = n - 1
        if num == tracker:
            count += 1
            tracker = n
        else:
            tracker = n
            count_consecutive.add(count)
            count = 0
    if count != 0:
        count_consecutive.add(count)
    return max(count_consecutive) + 1


if __name__ == '__main__':
    # n = [100, 4, 200, 1, 3, 2]
    # n = [0,3,7,2,5,8,4,6,0,1]
    n = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
    print(longest_consecutive(n))
