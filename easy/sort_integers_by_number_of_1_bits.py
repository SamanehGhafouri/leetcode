"""
You are given an integer array arr. Sort the integers in the array in ascending order by the number of 1's in their binary representation and in case of two or more integers have the same number of 1's you have to sort them in ascending order.

Return the array after sorting it.
"""
from typing import List


def sort_by_bits(arr: List[int]) -> List[int]:
    li_tuples_nums_binaries = []

    for i in arr:
        binary = bin(i)
        li_tuples_nums_binaries.append([binary.count('1'), i])

    li_tuples_nums_binaries.sort()
    result = []
    for b, i in li_tuples_nums_binaries:
        result.append(i)
    return result


if __name__ == '__main__':
    li = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(sort_by_bits(li))
