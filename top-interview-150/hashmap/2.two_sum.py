"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    dict_nums_indexes = {}
    for i in range(len(nums)):
        if nums[i] not in dict_nums_indexes:
            dict_nums_indexes[nums[i]] = [i]
        else:
            dict_nums_indexes[nums[i]].append(i)

    for i in range(len(nums)):
        second_num = target - nums[i]
        if second_num in dict_nums_indexes:
            if second_num != nums[i]:
                return [dict_nums_indexes[second_num][0], i]

            else:
                if len(dict_nums_indexes[second_num]) > 1:
                    return dict_nums_indexes[second_num]
                else:
                    i += 1


def two_sum_better_solution(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i in range(len(nums)):
        if target - nums[i] in seen:
            return [seen[target - nums[i]], i]
        else:
            seen[nums[i]] = i


if __name__ == '__main__':
    nums = [3, 2, 3]
    # nums = [3, 2, 4]
    # nums = [2, 5, 5, 11]
    # target = 10
    target = 6
    print(two_sum(nums, target))
