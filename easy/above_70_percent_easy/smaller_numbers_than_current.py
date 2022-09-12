"""
Given the array nums, for each nums[i] find out how many numbers
in the array are smaller than it. That is, for each nums[i] you have
to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.
"""
from typing import List


def smaller_numbers_than_current(nums: List[int]) -> List[int]:
    result = []
    sorted_elements_indexes = {}
    sorted_nums = sorted(nums)
    for i in range(len(sorted_nums)):
        if sorted_nums[i - 1] != sorted_nums[i]:
            sorted_elements_indexes[sorted_nums[i]] = i
        else:
            sorted_elements_indexes[sorted_nums[i]] = sorted_nums.index(sorted_nums[i])

    for i in nums:
        for k, v in sorted_elements_indexes.items():
            if i == k:
                result.append(v)
    return result


if __name__ == '__main__':
    li = [7, 7, 7, 7, 7]
    # expected result [0, 0, 0, 0, 0]
    # li_two = [8,1,2,2,3], expected = [4,0,1,1,3]

    print(smaller_numbers_than_current(li))
