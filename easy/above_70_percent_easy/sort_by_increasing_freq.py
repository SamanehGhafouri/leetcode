"""
Given an array of integers nums, sort the array in increasing order based on the frequency of the values.
If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.
"""
import collections
from typing import List


def frequency_sort(nums: List[int]) -> List[int]:
    dict_nums = collections.Counter(nums)
    result = []
    dict_by_freq = {}
    for key, value in dict_nums.items():
        if value not in dict_by_freq:
            dict_by_freq[value] = [key]
        else:
            dict_by_freq[value].append(key)
    sorted_dict_by_key = dict(sorted(dict_by_freq.items()))

    for key, values in sorted_dict_by_key.items():
        if len(values) > 1:
            values.sort()
            for v in values[::-1]:
                for n in range(key):
                    result.append(v)
        else:
            for n in range(key):
                result.append(values[0])
    return result


if __name__ == '__main__':
    nums = [-1, 1, -6, 4, 5, -6, 1, 4, 1]
    print(frequency_sort(nums))
