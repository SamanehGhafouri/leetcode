"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that
they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""

from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    result = []
    i = 0
    j = len(numbers) - 1

    while i < j:
        num_one = numbers[i]
        last_num = numbers[j]
        if num_one + last_num == target:
            result.append(i + 1)
            result.append(j + 1)
            break
        elif last_num > target - num_one:
            j -= 1
        elif last_num <= target - num_one:
            i += 1
    return result


if __name__ == '__main__':
    items = [
        ([0, 0, 3, 4], 0, [1, 2]),
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([5, 25, 75], 100, [2, 3])
    ]
    for item in items:
        print(two_sum(item[0], item[1]) == item[2])
